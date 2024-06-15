lst = list(input())
e = 0
n = 0
s = 0
el = 0
for i in lst:
    if ord("a")<=ord(i)<=ord("z") or ord("A")<=ord(i)<=ord("Z"):
        e+=1
    elif ord("1")<=ord(i)<=ord("9"):
        n+=1
    elif i==" ":
        s = lst.count(" ")
    else:
        el+=1
p = " ".join("%s"%i for i in [e,s,n,el])
print(p)
