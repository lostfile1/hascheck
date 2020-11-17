import os
import sys
import hashlib



with open(sys.argv[1],'rb') as flk:
    data = flk.read()

if sys.argv[2] =="md":
    print("md5:",hashlib.md5(data).hexdigest())
    
if sys.argv[2] =="sha":
    ret = 
    print("sha1:",hashlib.sha1(data).hexdigest())
