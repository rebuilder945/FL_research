s1=input()
s2=input()
lst=[s1,s2]
lst.sort()
if lst[0]=='blue' and lst[1]=='red':
    print('purple')
elif lst[0]=='blue' and lst[1]=='yellow':
    print('green')
elif lst[0]=='red' and lst[1]=='yellow':
    print('orange')
else:
    print('error')
