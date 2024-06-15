numbers=eval(input())#numbers=list(input())得到[[b,a,a,a]]则[,]a,b等都成了元素
b=len(numbers)
for i in numbers:
    if numbers.count(i)>1:
        while i in numbers:
            numbers.remove(i)
numbers.sort()
if numbers==[]:
    print("False")
else:
    for i in numbers[0:-1]:
        print(i,end=",")
    print(numbers[-1])



    



