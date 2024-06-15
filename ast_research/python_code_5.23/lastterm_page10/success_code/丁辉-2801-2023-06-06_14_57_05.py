def shuzi(m):
    for x in m:
        if x.isdigit():
            return True
def xiao(m):
    for x in m:
        if x.isalpha():
            if x.islower():
                return True
def da(m):
    for x in m:
        if x.isalpha():
            if x.isupper():
                return True
def long(m):
    if len(m)>=8:
        return True
def qi(m):
    st="~!@#$%^&*()_=-/,.?<>;:[]\|}{"
    for x in m:
        if x in st:
            return True
m=input()
n=0
if shuzi(m):
    n=n+1
if xiao(m):
    n=n+1
if da(m):
    n=n+1
if long(m):
    n=n+1
if qi(m):
    n=n+1
print(n)


