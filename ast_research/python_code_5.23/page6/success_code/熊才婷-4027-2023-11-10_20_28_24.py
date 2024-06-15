m=1
n=0
s=0
while m:
    num=input()
    if num!="#":
        s+=eval(num)
        n+=1
    else:
        m=0
print(n,s)
