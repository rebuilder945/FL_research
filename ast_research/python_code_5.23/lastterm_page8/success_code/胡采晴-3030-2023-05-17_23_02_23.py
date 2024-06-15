a = input()
b = eval(input())
c = a.split(",")
d = int(len(c))
e = []
for i in range (d):
    e.append(c[i],b[i])
def by_name(t):
    return t[0].lower() #使用lower将大写字母换成小写字母，如果都是大写或者小写字母可以直接用return t[0]
L=e
L1=sorted(L,key=by_name)
print(L1)   
