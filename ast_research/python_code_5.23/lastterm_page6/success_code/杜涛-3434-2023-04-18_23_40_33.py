list1={'red','blue'}
list2={'red','yellow'}
list3={'blue','yellow'}
a=input()
b=input()
c={a,b}

if c==list1:
    print("purple")
elif c==list2:
    print('orange')
elif c==list3:
    print('green')
else:
    print('error')
