from os import remove
from subprocess import list2cmdline


list1=eval(input())
a=list1.count(0)
while 0 in list1:
    list1.remove(0)
list2=[0]*a   
    
print(list1+list2)
