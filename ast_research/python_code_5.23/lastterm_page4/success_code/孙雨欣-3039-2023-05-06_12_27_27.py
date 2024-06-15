ls1=eval(input())
a=max(ls1)
count1=ls1.count(a)
b=min(ls1)
count2=ls1.count(b)
for i in range(count1):
    ls1.remove(a)
for i in range(count2):
    ls1.remove(b)
print(ls1)
    

