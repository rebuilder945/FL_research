num=eval(input())
mnum=""
while num!=0:
    k=num-(num//10)*10+5
    k=k%10
    mnum+=str(k)
    num=num//10
print(mnum)
