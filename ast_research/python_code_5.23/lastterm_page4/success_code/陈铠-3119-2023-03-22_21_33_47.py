lst=eval(input())
num=[]
lst.reverse()
for x in lst:
    if x not in num:
        num.append(x)
num.reverse()
print(num)

