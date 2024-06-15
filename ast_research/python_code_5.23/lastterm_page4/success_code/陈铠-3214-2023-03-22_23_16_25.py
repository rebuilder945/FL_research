lst=eval(input())
num=[]
for x in lst:
    if x==0:
        num.append(x)
while 0 in lst:
    lst.remove(0)
lst.extend(num)
print(lst)
