lst=eval(input())
num=[]
for x in lst:
    if x==0:
        num.append(x)
for i in lst:
    if i ==0:
        remove(i)
lst.extend(num)
