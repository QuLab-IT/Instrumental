import os
import os.path
import sys
from setuptools import setup, find_packages
from distutils.ccompiler import new_compiler
import distutils.cmd

# Metadata and dependencies are now primarily defined in pyproject.toml
# This setup.py handles dynamic parts: CFFI checks, extras_require generation, custom commands.

# Determine package directory
base_dir = os.path.dirname(__file__)
pkg_dir = os.path.join(base_dir, 'src', 'instrumental')

# Load dynamic metadata (e.g., version) if needed, although pyproject.toml might be static
# about = {}
# with open(os.path.join(pkg_dir, '__about__.py')) as f:
#     exec(f.read(), about)

# Load driver info for dynamic extras_require
try:
    with open(os.path.join(pkg_dir, 'driver_info.py')) as f:
        namespace = {}
        exec(f.read(), namespace)
        driver_info = namespace['driver_info']
    extras = {k:v['imports'] for k,v in driver_info.items()}
except FileNotFoundError:
    extras = {}

# Check for cffi and C compiler - needed early for potential messages
post_install_msgs = []
cffi_found = False
compiler_found = False
try:
    import cffi
    cffi_found = True
    try:
        new_compiler().compile(b'') # Simple check for compiler existence
        compiler_found = True
    except Exception:
        post_install_msgs.append(
            "No C compiler was found, so cffi modules may not build. If you would like to use "
            "cffi-based drivers that require compilation, first install a suitable compiler. "
            "See the cffi installation documentation for more details on installing an appropriate compiler "
            "for your platform.")
except ImportError:
    post_install_msgs.append(
        "Python cffi package was not installed, so cffi modules cannot be built. If you would like to use "
        "cffi-based drivers that require compilation, first install cffi and a suitable compiler, "
        "then reinstall Instrumental. See the cffi installation documentation for more details.")

# Function to find CFFI modules - call this only when needed
def find_cffi_modules():
    modules = []
    if cffi_found and compiler_found:
        cffi_build_root = os.path.join('src', 'instrumental')
        # Walk through the source directory
        for dirpath, dirnames, filenames in os.walk(cffi_build_root):
            # Check if a '_cffi_build' subdirectory exists
            if '_cffi_build' in dirnames:
                # Look for the build script (e.g., _build_pixelfly.py) in the current directory
                for fname in filenames:
                    if fname.startswith('_build_') and fname.endswith('.py'):
                        # Construct the path relative to the 'src' directory
                        rel_path = os.path.relpath(os.path.join(dirpath, fname), 'src')
                        # Format for cffi_modules: 'path/to/script.py:variable_name'
                        # Assuming the ffi object is created implicitly or via a standard name ('ffi'?)
                        # by the build_lib function used in _build_pixelfly.py.
                        # The ':ffi' suffix is standard for setuptools cffi integration.
                        modules.append(rel_path + ':ffi')
                        # Optional: break if only one build script per dir is expected
                        # break
    print(f"Found CFFI modules: {modules}") # Add print for debugging
    return modules

# Custom command to generate driver_info.py
class GenerateCommand(distutils.cmd.Command):
    description = 'generate the driver-info file'
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        self.announce("Generating driver_info.py...")
        from subprocess import call
        # Ensure parse_modules.py path is correct relative to setup.py execution
        script_path = os.path.join(pkg_dir, 'parse_modules.py')
        call([sys.executable, script_path])

# Determine if we are running a command that requires building CFFI modules
# Avoid running CFFI detection during 'egg_info', 'dist_info', 'clean' etc.
# This list might need adjustment based on observed pip/setuptools behavior
build_commands = ['build', 'build_py', 'build_ext', 'install', 'bdist', 'bdist_wheel', 'develop']
requires_cffi_build = any(cmd in sys.argv for cmd in build_commands)

setup_kwargs = {
    # Most metadata (name, version, author, etc.) and dependencies
    # are now defined in pyproject.toml.
    # Setuptools will automatically use them.

    # We still need to specify things that setuptools cannot (yet)
    # infer from pyproject.toml or that are dynamic:
    'packages': find_packages(where='src', exclude=['*._cffi_build']),
    'package_dir': {'': 'src'},
    'package_data': {
        '': ['*.h', '*.pyd'],
        'instrumental': ['instrumental.conf.default']
    },
    'extras_require': extras, # Dynamically generated
    'cmdclass': {
        'generate': GenerateCommand,
    },
    # Only include cffi_modules if we detected CFFI/Compiler AND a relevant command is run
    # 'setup_requires': ['cffi>=1.0.0'] if requires_cffi_build and cffi_found else [], # setup_requires is less preferred now
    'cffi_modules': find_cffi_modules() if requires_cffi_build else [],
}

if __name__ == '__main__':
    setup(**setup_kwargs)

    # Print post-install messages if any occurred during CFFI check
    # These messages are now generated earlier, print them regardless of build outcome
    if post_install_msgs:
        print("\n" + "\n\n".join(post_install_msgs))
