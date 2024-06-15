def chengji(s):
    return s[1]
a=input().split(",")
b=list(map(int,input().split(",")))
ls=list(zip(a,b))
for i in range(len(ls)):
    ls[i]=list(ls[i])
ls.sort(key=chengji)
print(ls)

