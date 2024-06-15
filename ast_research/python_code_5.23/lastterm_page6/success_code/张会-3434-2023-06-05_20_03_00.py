a=input()
b=input()
ls=[]
ls.append(a)
ls.append(b)
m=set(ls)
x={'red','blue'}
y={'red','yellow'} 
z={'blue','yellow'}
if m==x:
    print('purple')
elif m==y:
    print('orange') 
elif m==z:
    print('green')
else:
    print('error')      
