from email.utils import parsedate_to_datetime
from operator import truediv


def prime(num):
    i=2
    for i in range(2,num):
        if num%i==0:
            return False
        i=i+1
    return True
lst=eval(input())
lst2=[]
for a in lst:
    i=2
    if a>1 and prime(a)==True:
        lst2.append(a)
print(lst2)

