import torch

from torch import nn
from torch.autograd import Function
#from models.py_utils._cpools import top_pool, bottom_pool, left_pool, right_pool

#os.system(f"python {libdir}/setup.py build_ext --inplace")

#def load_lib(libname):
#    import os, ctypes
#    #libdir = os.path.dirname(__file__)
#    libdir = "."
#    libpath = os.path.join(libdir, libname)
#    return ctypes.cdll.LoadLibrary("./"+libpath)

#top_pool = load_lib('top_pool.cpython-37m-x86_64-linux-gnu.so')
#bottom_pool = load_lib('bottom_pool.cpython-37m-x86_64-linux-gnu.so')
#left_pool = load_lib('left_pool.cpython-37m-x86_64-linux-gnu.so')
#right_pool = load_lib('right_pool.cpython-37m-x86_64-linux-gnu.so')

import os, torch.utils.cpp_extension
libdir = os.path.dirname(__file__)
top_pool = torch.utils.cpp_extension.load(name="top_pool", sources=[libdir+"/src/top_pool.cpp"])
bottom_pool = torch.utils.cpp_extension.load(name="top_pool", sources=[libdir+"/src/bottom_pool.cpp"])
left_pool = torch.utils.cpp_extension.load(name="top_pool", sources=[libdir+"/src/left_pool.cpp"])
right_pool = torch.utils.cpp_extension.load(name="top_pool", sources=[libdir+"/src/right_pool.cpp"])

class TopPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = top_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input  = ctx.saved_variables[0]
        output = top_pool.backward(input, grad_output)[0]
        return output

class BottomPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = bottom_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input  = ctx.saved_variables[0]
        output = bottom_pool.backward(input, grad_output)[0]
        return output

class LeftPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = left_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input  = ctx.saved_variables[0]
        output = left_pool.backward(input, grad_output)[0]
        return output

class RightPoolFunction(Function):
    @staticmethod
    def forward(ctx, input):
        output = right_pool.forward(input)[0]
        ctx.save_for_backward(input)
        return output

    @staticmethod
    def backward(ctx, grad_output):
        input  = ctx.saved_variables[0]
        output = right_pool.backward(input, grad_output)[0]
        return output

class TopPool(nn.Module):
    def forward(self, x):
        return TopPoolFunction.apply(x)

class BottomPool(nn.Module):
    def forward(self, x):
        return BottomPoolFunction.apply(x)

class LeftPool(nn.Module):
    def forward(self, x):
        return LeftPoolFunction.apply(x)

class RightPool(nn.Module):
    def forward(self, x):
        return RightPoolFunction.apply(x)
