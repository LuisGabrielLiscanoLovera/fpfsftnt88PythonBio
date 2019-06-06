import os
import sys
from ctypes import *
import ctypes
#http://buontempoconsulting.blogspot.com/2017/06/call-dll-from-python.html
#http://www.pe-explorer.com/peexplorer-download.htm
#https://www.nirsoft.net/utils/registered_dll_view.html
lib = cdll.LoadLibrary('Nffv.dll')
lb = ctypes.WinDLL('NffvJavaNative.dll')
print(dir(lb))
proto = ctypes.WINFUNCTYPE(ctypes.c_int)
params = ()
answer = proto(("NffvEnroll", lib), params)
print (answer)
import pprint

pprint.pprint(lb.__dict__)

#Regsvr32 
from ppretty import ppretty


class A(object):
    s = 5

    def __init__(self):
        self._p = 8

    @property
    def foo(self):
        return range(10)


print (ppretty(lib._FuncPtr(), indent='    ', depth=2, width=30, seq_length=6,
              show_protected=True, show_private=False, show_static=True,
              show_properties=True, show_address=True))


print (ppretty(lib, indent='    ', depth=2, width=30, seq_length=6,
              show_protected=True, show_private=False, show_static=True,
              show_properties=True, show_address=True))





print (ppretty(lb, indent='    ', depth=2, width=30, seq_length=6,
              show_protected=True, show_private=False, show_static=True,
              show_properties=True, show_address=True))
