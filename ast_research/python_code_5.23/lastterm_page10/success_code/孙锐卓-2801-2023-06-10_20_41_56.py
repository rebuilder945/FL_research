def f1(x):
    t = 0
    for i in x:
        if '0' <= i <= '9':
            t = 1
            break
    return t

def f2(x):
    t = 0
    for i in x:
        if 'a' <= i <= 'z':
            t = 1
            break
    return t

def f3(x):
    t = 0
    for i in x:
        if 'A' <= i <= 'Z':
            t = 1
            break
    return t


def f4(x):
    t = 0
    if len(x) >= 8:
        t = 1
    return t

def f5(x):
    t = 0
    s ='~!@#$%^&*()_=-/,.?<>;:[]|'
    for i in x:
        if i in s or ord(i)==92 or 123<=ord(i)<=125:
            t = 1
            break
    return t

x= input()
a = f1(x)+f2(x)+f3(x)+f4(x)+f5(x)
print(a)



