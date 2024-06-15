from distutils.log import error
from operator import index
from os import lstat
from sunau import AUDIO_FILE_ENCODING_MULAW_8


list1=eval(input())
lst=[]
n,m=eval(input())
k=len(list1)
if n<0:
    n=len(list1)+n+1
if m<0:
    m=len(list1)+m+1


if n>=0 and n<=len(list1):
    if m>len(list1):
        lst=lst+list1[0:n]
    if m<=len(list1):
        lst=lst+list1[0:n]+list1[m:]
        print(lst)
else :
    print("error")        
