a=input()
b=len(a)
ls1=[0 for i in range(b)]
if a[0].isdigit():
    ls1[0]=1
for i in range(1,len(a)):
    if a[i].isdigit():
        ls1[i]=ls1[i-1]+1
max=1
n=0
f=False
for i in range(b):
    if ls1[i]>=max:
        max=ls1[i]
        n=i
        f=True
if f:    
    print(ls1[i-max+1:i+1])
else:
    print('No digits')
            
