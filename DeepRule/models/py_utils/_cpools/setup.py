from setuptools import setup
from torch.utils.cpp_extension import BuildExtension, CppExtension

import os
libdir = os.path.dirname(__file__)

setup(
    name="cpools",
    ext_modules=[
        CppExtension("top_pool", [libdir+"/src/top_pool.cpp"]),
        CppExtension("bottom_pool", [libdir+"src/bottom_pool.cpp"]),
        CppExtension("left_pool", [libdir+"src/left_pool.cpp"]),
        CppExtension("right_pool", [libdir+"src/right_pool.cpp"])
    ],
    cmdclass={
        "build_ext": BuildExtension
    }
)
