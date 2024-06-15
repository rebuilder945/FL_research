def hanshu(a):
    if a<=2:
        return a
    else:
        return hanshu(a-1)+hanshu(a-2)
n=eval(input())
res=0
for i in range(1,n+1):
    res+=hanshu(i+1)/hanshu(i)
print("%.4f"%res)


