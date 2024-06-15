from math import fabs
from sys import flags


s = list(eval(input()))
h = []
s.sort()
for i in range(len(s)):
    flag = False
    for j in range(len(s)):
        if i!=j and s[i]==s[j]:
            flag = True
            break
    if flag is False:
        h.append(s[i])
if h == []:
   print("False")
else:
    for x in range(len(h)-1):
         print(h[x],end=",")
    print(h[-1])
