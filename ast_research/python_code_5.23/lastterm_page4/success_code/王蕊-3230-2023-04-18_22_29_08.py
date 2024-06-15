ls=eval(input())
ls.sort(reverse=True)
a=0
n=0
b=len(ls)
for x in ls:
    while a<b:
        n+=x*(10**b)
        a+=1
        b-=1
print(n)

