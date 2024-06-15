x=input()
a=0
b=0
c=0
d=0
for i in range(52):
    a+=x.count(chr(65+i))
for i in range(9):
    b+=x.count(str(i))
c=x.count(" ")
d=len(x)-a-b-c
print(a,c,b,d)










        



    








