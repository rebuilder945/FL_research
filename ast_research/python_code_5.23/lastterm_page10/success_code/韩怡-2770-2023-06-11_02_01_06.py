def bwc(a,b):
    if len(a)==len(b):
        for i in a:
            if a.count(i)!=b.count(i):
                return False
        return True
    else:
        return False
a=input()
b=input()
print(bwc(a,b))

