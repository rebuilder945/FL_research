a=input()
b=input()
h1={'red','blue'}
h2={'red','yellow'}
h3={'yellow','blue'}
if set(a,b)==h1:
    print('purple') 
elif set(a,b)==h2:
    print('orange') 
elif set(a,b)==h3:
    print('green')
else:
    print('error') 


