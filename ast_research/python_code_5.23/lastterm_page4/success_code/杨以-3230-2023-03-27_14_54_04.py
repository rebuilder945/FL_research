list=eval(input())
a=0
while len(list)>0:
    b=max(list)
    a=a+b*(10**(len(list)-1))
    list.remove(b)
print(a)


