def bianwei(a,b):
    flag= 0
    for x in a:
        if b.count(x)!=a.count(x) or len(a)!=len(b):
            flag = 1
            break
        else:
            flag = 0
    return flag
a = input()
b = input()
c = bianwei(a,b)
if c == 0:
    print("True")
else:
    print("False")
