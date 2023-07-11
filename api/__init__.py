from fastapi import FastAPI
from ctypes import *

app = FastAPI()

libAiDB = cdll.LoadLibrary("/Users/hulk/Documents/DX_Work/CodeZoo/AIDeployBox/build/source/libAiDB_C.dylib")

AiDBCreate = libAiDB.AiDBCreate
AiDBCreate.restype = c_void_p

AiDBFree = libAiDB.AiDBFree
AiDBFree.argtypes = [c_void_p]

AiDBRegister = libAiDB.AiDBRegister
AiDBRegister.argtypes = [c_void_p, c_char_p]
AiDBRegister.restype = int

AiDBUnRegister = libAiDB.AiDBUnRegister
AiDBUnRegister.argtypes = [c_char_p]
AiDBUnRegister.restype = int

AiDBForward = libAiDB.AiDBForward
AiDBForward.argtypes = [c_void_p, c_char_p, c_char_p, c_char_p, c_int, POINTER(c_int)]
AiDBForward.restype = int

g_ins = AiDBCreate()

from . import aidb, types
from .aidb import *
from .types import *

__all__ = (
    types.__all__
)

