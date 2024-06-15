numbers=eval(input())#numbers=list(input())得到[[b,a,a,a]]则[,]a,b等都成了元素
a=[]
for i in numbers:
    if numbers.count(i)>1:
        a.append(i)
b=[]
for i in numbers:
    if i in numbers and i not in a:
        b.append(i)
b.sort()
print(b)
print(a)
if b==[]:
    print("False")
else:
    for i in b[0:-1]:
        print(i,end=",")
    print(b[-1])



    



