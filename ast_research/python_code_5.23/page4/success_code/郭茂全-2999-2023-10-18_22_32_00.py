a=input()
n,m=eval(input())
list=a.split(' ')
list=list[:]
b=list[n]
list[n]=list[m]
list[m]=b
print(a)
