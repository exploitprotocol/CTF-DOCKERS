#!/usr/bin/env python2.7

from Crypto.Util.number import *
from os import urandom
import sys
import ecauth
from secret import flag, n

class Unbuffered(object):
   def __init__(self, stream):
       self.stream = stream
   def write(self, data):
       self.stream.write(data)
       self.stream.flush()
   def writelines(self, datas):
       self.stream.writelines(datas)
       self.stream.flush()
   def __getattr__(self, attr):
       return getattr(self.stream, attr)

sys.stdout = Unbuffered(sys.stdout)

class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'


p = 89953523493328636138979614835438769105803101293517644103178299545319142490503
a = p-3
b = 28285296545714903834902884467158189217354728250629470479032309603102942404639
ec = ecauth.CurveFp(p, a, b)

# Point P on the curve
_Px = 0x337ef2115b4595fbd60e2ffb5ee6409463609e0e5a6611b105443e02cb82edd8L
_Py = 0x1879b8d7a68a550f58166f0d6b4e86a0873d7b709e28ee318ddadd4ccf505e1aL

# n is the order of the subgroup generated by (_Px, _Py)
assert ec.contains_point(_Px, _Py)

# x is the session-secret key
x = getPrime(254)

assert x < n

point_P = ecauth.Point(ec, _Px, _Py, n)
assert point_P * n == ecauth.INFINITY

publickey = ecauth.Public_key(point_P)
privatekey = ecauth.Private_key(publickey, x)

"""
You can use the _sign method in ecauth to sign for authentication process.
But remember,
You must have the same x as generated in this script to successfully authenticate!
"""

print colors.orange + "-"*26 + "Welcome to EC-Auth mechanism" + "-"*26 + colors.reset
point_Q = x * point_P
print "\nHere is my point Q = x * P: ", point_Q

try:
    _Rx = raw_input("\nGive me x-coordinate of point R = r * P (in hex without 0x): ")
    _Ry = raw_input("Give me y-coordinate of point R = r * P (in hex without 0x): ")
    s = raw_input("Give me s = r + x (in hex without 0x): ")
    _Rx = int(_Rx, 16)
    _Ry = int(_Ry, 16)
    s = int(s, 16)
except:
    print colors.red + "\nEnter proper hex values!" + colors.reset
    sys.exit()

if not ec.contains_point(_Rx, _Ry):
    print colors.red + "\nPoint R does not lie on the curve!" + colors.reset
    sys.exit()

point_R = ecauth.Point(ec, _Rx, _Ry)
assert n * point_R == ecauth.INFINITY

obj1 = ecauth.Handshake(point_Q, point_R, s)
if publickey._verify(obj1):
    print colors.green + "\nHere, take your flag: " + flag + colors.reset
else:
    print colors.red + "\nI knew you would fail" + colors.reset
    sys.exit()
