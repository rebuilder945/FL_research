a=eval(input())
b=a[::-1]
dp=[]
for i in range(len(b)):
    if b[i] in dp:
        pass
    else:
        dp.append(b[i])
print(dp[::-1])
