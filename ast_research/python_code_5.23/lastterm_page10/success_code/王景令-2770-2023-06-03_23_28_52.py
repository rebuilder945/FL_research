a = input()
b = input()
def asd(a,b):
    for i in a:
        if i in b:
            if a.count(i) == b.count(i):
                continue
            else:
                return False
        else:
            return False
    return True
print(asd(a,b))


