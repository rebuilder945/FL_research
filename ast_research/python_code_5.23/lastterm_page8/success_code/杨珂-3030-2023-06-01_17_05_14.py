def chengji(s):
    s=[1]
    return s
a=input().split(",")
b=input().split(",")
ls=list(zip(a,b))
for i in range(len(ls)):
    ls[i]=list(ls[i])
ls.sort(key=chengji)
print(ls)

