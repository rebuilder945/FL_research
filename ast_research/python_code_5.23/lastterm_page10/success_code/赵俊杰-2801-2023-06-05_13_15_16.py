def num(ls):
    for x in ls:
        p=0
        if x.isdigit():
            p=1
            break
        else:
            pass
    return p
def other(ls):
    for x in ls:
        q=0
        if x.isdigit():
            pass
        elif x.isalpha():
            pass
        else:
            q=1
            break
    return q
def eng1(ls):
    for x in ls:
        y=0
        if x.isalpha():
            if x.islower():
                y=1
                break
            else:
                pass
    return y
def eng2(ls):
    for x in ls:
        p=0
        if x.isalpha():
            if x.isupper():
                p=1
                break
            else:
                pass
    return p
secret=input()
a=len(secret)
if a>=8:
    a=1
else:
    a=0
all=a+num(secret)+eng1(secret)+eng2(secret)+other(secret)
print(all)
print(num(secret))
print(eng1(secret))
print(eng2(secret))
print(other(secret))
