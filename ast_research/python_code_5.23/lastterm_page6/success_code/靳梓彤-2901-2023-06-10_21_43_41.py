count=0
res=0
num=""
while True:
    num=input()
    if num=="#":
        break
    res+=eval(num)
    count+=1
print(count,res)


