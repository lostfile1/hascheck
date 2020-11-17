import os
import sys
import hashlib



with open(sys.argv[1],'rb') as flk:
    data = flk.read()

if sys.argv[2] =="md":
    print("md5:",hashlib.md5(data).hexdigest())
    
elif sys.argv[2] =="sha": 
    print("sha1:",hashlib.sha1(data).hexdigest())

elif sys.argv[2] =="sha5":
    print("sha5:",hashlib.sha512(data).hexdigest())
