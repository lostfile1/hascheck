import os
import sys
import hashlib



with open(sys.argv[1],'rb') as flk:
    data = flk.read()

if sys.argv[2] =="md":
    ret = hashlib.md5(data).hexdigest()
    print("md5:",ret)
    
if sys.argv[2] =="sha":
    ret = hashlib.sha1(data).hexdigest()
    print("sha1:",ret)