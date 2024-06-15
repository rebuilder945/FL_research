n=input() 
ls1=[]
ls2=[]
while n!='ok':
    key,value=n.split()
    ls1.append(key)
    ls2.append(value)
    n=input()
ls2=list(map(int,ls2))
print(ls1)
print(ls2)
if 'India' in ls1:
    print('yes')
else:
    print('no')
x=0
for i in ls2:
    x+=i
print(x)
