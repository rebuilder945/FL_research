count=0
sum=0
while True:
    num=input()
    if num=="#":
        break
    num=int(num)
    count+=1
    sum+=num
h="%d %d"%(count,sum)
print(h)
