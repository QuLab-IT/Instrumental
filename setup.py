import os
import os.path
import sys
from setuptools import setup, find_packages
from distutils.ccompiler import new_compiler
import distutils.cmd

description = "Library with high-level drivers for lab equipment"
classifiers = [
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Intended Audience :: Science/Research',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
]

# Load metadata from __about__.py
base_dir = os.path.dirname(__file__)
pkg_dir = os.path.join(base_dir, 'src', 'instrumental')
about = {}
with open(os.path.join(pkg_dir, '__about__.py')) as f:
    exec(f.read(), about)

# Load driver info
try:
    with open(os.path.join(pkg_dir, 'driver_info.py')) as f:
        namespace = {}
        exec(f.read(), namespace)
        driver_info = namespace['driver_info']
    extras = {k:v['imports'] for k,v in driver_info.items()}
except FileNotFoundError:
    extras = {}

# Check for cffi
post_install_msgs = []
try:
    import cffi

    try:
        new_compiler().compile(b'')
        build_cffi_modules = True
    except:
        build_cffi_modules = False
        post_install_msgs.append(
            "No C compiler was found, so cffi modules were not built. If you would like to use "
            "cffi-based drivers that require compilation, first install a suitable compiler, "
            "then reinstall Instrumental. See the cffi installation documentation for more details "
            "on installing an appropriate compiler for your platform.")
except:
    build_cffi_modules = False
    post_install_msgs.append(
        "Python cffi was not installed, so cffi modules were not built. If you would like to use "
        "cffi-based drivers that require compilation, first install cffi and a suitable compiler, "
        "then reinstall Instrumental. See the cffi installation documentation for more details on "
        "installing an appropriate compiler for your platform.")


# Find all cffi build scripts
keywords = {}
if build_cffi_modules:
    keywords['setup_requires'] = ["cffi>=1.0.0"]
    modules = []
    for dirpath, dirnames, filenames in os.walk('instrumental'):
        basename = os.path.basename(dirpath)
        for fname in filenames:
            if basename == '_cffi_build' and fname.startswith('build_'):
                modules.append(os.path.join(dirpath, fname) + ':ffi')
    keywords['cffi_modules'] = modules


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
        call([sys.executable, os.path.join(pkg_dir, 'parse_modules.py')])


if __name__ == '__main__':
    with open('README.rst') as f:
        readme_txt = f.read()
    desc = 'Instrumental\n============\n' + readme_txt.partition('====\n')[-1]

    setup(
        name = about['__distname__'],
        version = about['__version__'],
        packages = find_packages(where='src', exclude=['*._cffi_build']),
        package_dir = {'': 'src'},
        package_data = {
            '': ['*.h', '*.pyd'],
            'instrumental': ['instrumental.conf.default']
        },
        author = about['__author__'],
        author_email = about['__email__'],
        description = description,
        long_description = desc,
        long_description_content_type = 'text/x-rst',
        url = about['__url__'],
        license = about['__license__'],
        classifiers = classifiers,
        install_requires = ['numpy', 'scipy', 'pint>=0.7', 'future'],
        extras_require = extras,
        cmdclass={
            'generate': GenerateCommand,
        },
        **keywords
    )

    if post_install_msgs:
        print("\n" + "\n\n".join(post_install_msgs))
