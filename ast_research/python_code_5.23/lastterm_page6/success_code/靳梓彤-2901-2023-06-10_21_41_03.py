count=0
res=0
num=""
while True:
    num=input()
    if num=="#":
        break
    res=eval(num)
    res=list(res)
    res1=res[-2:0]
    res2=sum(res1)
    count+=1
print(count,res1)
