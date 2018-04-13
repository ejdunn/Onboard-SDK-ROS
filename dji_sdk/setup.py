from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

setup_args = generate_distutils_setup(
    packages=['dji_sdk'],
    package_dir={'':'../../../catkin_sensors/devel/lib'},
)

setup(**setup_args)

