#def __bootstrap__():
#    global __bootstrap__, __loader__, __file__
#    import sys, pkg_resources, imp
#    __file__ = pkg_resources.resource_filename(__name__, 'top_pool.cpython-36m-x86_64-linux-gnu.so')
#    __loader__ = None; del __bootstrap__, __loader__
#    imp.load_dynamic(__name__,__file__)
#__bootstrap__()
import os
import ctypes

def load_lib(libname):
    libdir = os.path.dirname(__file__)
    libpath = os.path.join(libdir, libname)
    os.listdir(libpath)
#    return ctypes.cdll.LoadLibrary(libpath)

top_pool = load_lib('top_pool.cpython-36m-x86_64-linux-gnu.so')