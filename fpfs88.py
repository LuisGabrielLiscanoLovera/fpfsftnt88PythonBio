import os
import sys
from ctypes import *
import ctypes
from ppretty import ppretty
#http://buontempoconsulting.blogspot.com/2017/06/call-dll-from-python.html
#http://www.pe-explorer.com/peexplorer-download.htm
#https://www.nirsoft.net/utils/registered_dll_view.html
m_iEnrollTimeout = 5000
m_iVerifyTimeout = 2000







lib = cdll.LoadLibrary('Nffv.dll')
#lb = ctypes.WinDLL('NffvJavaNative.dll')
#lb =  cdll.LoadLibrary('NffvJavaNative.dll')
#print(dir(lb))
proto = ctypes.WINFUNCTYPE(ctypes.c_int)
params = ()
answer = proto(("NffvGetAvailableScannerModulesA", lib), params)
#answer = proto(("?Java_com_neurotechnology_Nffv_Nffv_getMaxUserCount0@@YGJPAUJNIEnv_@@PAV_jclass@@@Z", lb), params)
print (answer)


NffvGetAvailableScannerModulesA      = lib['NffvGetAvailableScannerModulesA']
print (type(NffvGetAvailableScannerModulesA))
#NffvGetAvailableScannerModulesA()

NffvCancel          = lib['NffvCancel']
#NffvCancel()

NffvClearUsers      = lib['NffvClearUsers']
#NffvClearUsers()

print ("*****************************************")
print (ppretty(NffvGetAvailableScannerModulesA, indent='    ', depth=2, width=30, seq_length=6,
              show_protected=True, show_private=True, show_static=True,
              show_properties=True, show_address=True))

"""
NffvCancel                        = Cancels a fingerprint enrollment or verification operation.   
NffvClearUsers                    = Removes all the users which were enrolled to a database.       
NffvEnroll                        = Gets a fingerprint from a scanner and saves it to a database.   

NffvFreeMemory                    = Releases memory allocated by the NffvGetAvailableScannerModules function..       
NffvGetAvailableScannerModulesA   = Returns available fingerprint scanner modules for usage in the Free Fingerprint Verification SDK.                       
NffvGetAvailableScannerModulesW   = Returns available fingerprint scanner modules for usage in the Free Fingerprint Verification SDK.                       
NffvGetErrorMessageA              = Gets an error message. Use this function for errors handling.             
NffvGetErrorMessageW              = Gets an error message. Use this function for errors handling.             
NffvGetMatchingThreshold          = Gets the minimum similarity value that verification function uses to determine whether the fingerprint matches.                 
NffvGetQualityThreshold           = Gets an image quality threshold.               
NffvGetUser                       = Gets the information from a users list about an enrolled user.   
NffvGetUserById                   = Returns user details by the Id from a database.       
NffvGetUserCount                  = Retrieves the number of users enrolled to database.         
NffvGetUserIndexById              = Retrieves the index from users list of a user indica             
NffvInitializeA                   = Initializes the FFV. This function as a parameters takes a name and a password of a previously created database or creates a new database.
NffvInitializeW                   = Initializes the FFV. This function as a parameters takes a name and a password of a previously created database or creates a new database.
NffvRemoveUser                    = Removes a user from users list (database).NffvSetMatchingThreshold ( seepage 29)Sets the minimum similarity value that verification function uses todetermine whether the fingerprint matches.
NffvSetQualityThreshold           = Sets an image quality threshold.
NffvUninitialize                  = Releases memory resources.
NffvUserGetHBitmap                = Gets a handle to the bitmap of a user fingerprint.
NffvUserGetImage                  = Gets a user's fingerprint image which was enrolled to a database.
NffvVerify                        = Compares a captured fingerprint with the one that was enrolled to a database before in order to determine whether two match.

"""



'''import pprint
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

print (ppretty(NffvCancel, indent='    ', depth=2, width=30, seq_length=6,
              show_protected=True, show_private=False, show_static=True,
              show_properties=True, show_address=True))
'''
