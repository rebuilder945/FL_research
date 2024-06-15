lst = list(input())
e = 0
n = 0
el = 0
s = lst.count(" ")
for i in lst:
    if ord("a")<=ord(i)<=ord("z") or ord("A")<=ord(i)<=ord("Z"):
        e+=1
    elif 0<=int(i)<=9:
        n+=1
    else:
        el+=1
p = "".join("%s"%i for i in [e,s,n,el])
print(p)
