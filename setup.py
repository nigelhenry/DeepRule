from setuptools import setup, find_packages

setup(
    name='deeprule',
    version='0.1',
    package_data={"": ["DeepRule/models/py_utils/_cpools/src/*.cpp","models/py_utils/_cpools/src/*.cpp"]},
    include_package_data=True
)
