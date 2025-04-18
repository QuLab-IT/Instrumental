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

# Check for cffi and C compiler
post_install_msgs = []
try:
    import cffi
    try:
        new_compiler().compile(b'')
        build_cffi_modules = True
    except Exception:
        build_cffi_modules = False
        post_install_msgs.append(
            "No C compiler was found, so cffi modules were not built. If you would like to use "
            "cffi-based drivers that require compilation, first install a suitable compiler, "
            "then reinstall Instrumental. See the cffi installation documentation for more details "
            "on installing an appropriate compiler for your platform.")
except ImportError:
    build_cffi_modules = False
    post_install_msgs.append(
        "Python cffi was not installed, so cffi modules were not built. If you would like to use "
        "cffi-based drivers that require compilation, first install cffi and a suitable compiler, "
        "then reinstall Instrumental. See the cffi installation documentation for more details on "
        "installing an appropriate compiler for your platform.")

# Find all cffi build scripts if applicable
keywords = {}
if build_cffi_modules:
    # setup_requires is deprecated in favor of pyproject.toml build-system.requires
    # but cffi_modules needs to be passed to setup()
    modules = []
    # Assuming the source layout is src/instrumental
    cffi_build_root = os.path.join('src', 'instrumental')
    for dirpath, dirnames, filenames in os.walk(cffi_build_root):
        basename = os.path.basename(dirpath)
        for fname in filenames:
            if basename == '_cffi_build' and fname.startswith('build_'):
                # Path relative to package root ('src') expected by cffi?
                # Adjust if needed based on how cffi expects the path.
                rel_path = os.path.relpath(dirpath, 'src')
                modules.append(os.path.join(rel_path, fname) + ':ffi')
    if modules:
        keywords['cffi_modules'] = modules

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


if __name__ == '__main__':
    # Long description can still be read dynamically if desired,
    # though pyproject.toml's 'readme' field is preferred
    # with open('README.rst') as f:
    #     long_desc = f.read()

    setup(
        # Most metadata (name, version, author, etc.) and dependencies
        # are now defined in pyproject.toml.
        # Setuptools will automatically use them.

        # We still need to specify things that setuptools cannot (yet)
        # infer from pyproject.toml or that are dynamic:
        packages=find_packages(where='src', exclude=['*._cffi_build']),
        package_dir={'': 'src'},
        package_data={
            '': ['*.h', '*.pyd'],
            'instrumental': ['instrumental.conf.default']
        },
        extras_require=extras, # Dynamically generated
        cmdclass={
            'generate': GenerateCommand,
        },
        # Pass cffi_modules if they were found
        **keywords
    )

    # Print post-install messages if any occurred during CFFI check
    if post_install_msgs:
        print("\n" + "\n\n".join(post_install_msgs))
