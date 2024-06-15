numbers=eval(input())#numbers=list(input())得到[[b,a,a,a]]则[,]a,b等都成了元素
a=[]
for i in numbers:
    if numbers.count(i)>1:
        a.append(i)
b=[]
for i in numbers:#若无此步骤，则出错，i为上一次循环i的最后取值
    if i in numbers and i not in a:#可以如此写【1,1
        b.append(i)
b.sort()
if b==[]:
    print("False")
else:
    for i in b[0:-1]:
        print(i,end=",")
    print(b[-1])



    



