from setuptools import setup, find_packages

setup(
    name='deeprule',
    version='0.1',
    package_data={"": ["models/py_utils/_cpools/src/*.cpp",
                       "models/py_utils/_cpools/*.so",
                       "pycocotool/*.so",
                      "config/*.json"]},
    include_package_data=True,
    install_requires = ["azureml.core"]
)
