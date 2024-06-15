lst=eval(input())
lst2=[]
b=""
while len(lst)>=1:
    a=max(lst)
    lst.remove(a)
    lst2.append(a)
for i in range(len(lst2)):
    b+="lst[i]"
print(eval(b))
