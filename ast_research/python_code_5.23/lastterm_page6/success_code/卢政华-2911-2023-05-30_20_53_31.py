num=list(eval(input()))
for i in range(num):
    num=(num[i]+5)/10
num[0],num[-1]=num[-1],num[0]
num[1],num[-2]=num[-2],num[1]
print(num)
