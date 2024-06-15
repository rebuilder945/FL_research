num=str(input())
new1=[]
for i in num:
    i=int(i)
    i1=i+5
    i2=i1%10
    new1.append(i2)
    new1.reverse()
print("".join(map(str,new1)))
