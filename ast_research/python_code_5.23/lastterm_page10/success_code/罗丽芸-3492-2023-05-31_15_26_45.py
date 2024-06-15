a=input()
def f(x):
    for i in x:
        if x.count(i)==1:
            return i
if a=='':
    print('None')
else:
    print(f(a))

