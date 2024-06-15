lst=eval(input())
s=[]
for i in lst:
    if i==0:
        s.append(i)
        lst.remove(0)
print(lst+s)
