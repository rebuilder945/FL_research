count=0
res=0
num=""
while True:
    num=input()
    if num=="#":
        break
    num1=eval(num)
    num1=int(num1)
    res=sum(num1)
    count+=1
print(count,res)
