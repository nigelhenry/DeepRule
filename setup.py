from setuptools import setup, find_packages

setup(
    name='deeprule',
    version='0.1',
    package_data={"": ["models/py_utils/_cpools/src/*.cpp",
                      "pycocotool/_mask.pyx",
                      "pycocotool/maskApi.h"]},
    include_package_data=True
)
