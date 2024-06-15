def R(a,b):
    s = 0
    if b == 1 :
        s = len(a)
    else:
        for i in a:
            if type(i)==list:
                s += R(i,b-1)
    return s
a=eval(input())
b=eval(input())
print(R(a,b))

