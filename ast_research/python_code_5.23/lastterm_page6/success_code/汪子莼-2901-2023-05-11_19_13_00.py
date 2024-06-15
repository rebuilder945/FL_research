count=0
res=0
while True:
    a=input()
    if a=="#":
        break
    res+=eval(a)
    count+=1
print(count,res)
