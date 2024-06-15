def bianwc(a,b):
    ls1=list(a)
    ls2=list(b)
    ls1.sort()
    ls2.sort()
    if ls1==ls2:
        return True
    return False
a=input()
b=input()
print(bianwc(a,b))
