list=input().split(" ")#split里面不可“”可以“ ”
list1=input().split(" ")
n=eval(list1[0])
m=eval(list1[1])
a=list[n]
b=list[m]
list[n]=b
list[m]=a
print(list)

