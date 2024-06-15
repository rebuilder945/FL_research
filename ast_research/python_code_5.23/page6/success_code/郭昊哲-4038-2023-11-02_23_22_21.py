x=input()
a=0
b=0
c=0
d=0
for i in range(26):
    a+=x.count(chr(97+i))
for i in range(9):
    b+=x.count(str(i))
c=x.count(" ")
d=len(x)-a-b-c
print(a,c,b,d)










        



    








