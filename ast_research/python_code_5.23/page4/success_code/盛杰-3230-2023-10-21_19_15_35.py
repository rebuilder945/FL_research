ls=eval(input())
ls.sort()
num=0
for i in range(len(ls)):
    num=num+(ls[i]*10**i)
print(num)

