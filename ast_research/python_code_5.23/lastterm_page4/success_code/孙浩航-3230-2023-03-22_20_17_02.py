from audioop import reverse
from re import A


list1=eval(input())
list1.sort(reverse=True)
a=""
for x in list1:
    a=a+str(x)
print(a)
    


