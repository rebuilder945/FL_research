def q(ls1):
    f=False
    for i in ls1:
        if i.isdigit():
            f=True
    return f
def p(ls1):
    f=False
    for i in ls1:
        if i.islower():
            f=True
    return f
def o(ls1):
    f=False
    for i in ls1:
        if not (i.isdigit() and i.isalpha()):
            f=True
    return f
def e(ls1):
    f=False
    for i in ls1:
        if i.isupper():
            f=True
    return f
w=0
a=list(input())
if q(a):
    w+=1
if o(a):
    w+=1
if p(a):
    w+=1
if e(a):
    w+=1
if len(a)>=8:
    w+=1
print(w)


