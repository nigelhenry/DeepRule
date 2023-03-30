from setuptools import setup, find_packages

setup(
    name='deeprule',
    version='0.1',
    include_package_data=True,
    package_data={"": ["DeepRule/models/py_utils/_cpools/*.  so"]}
)
