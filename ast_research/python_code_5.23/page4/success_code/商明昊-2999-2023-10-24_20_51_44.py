list=input()
m,n=eval(input())
t=list.split()
a=t[m]
t[m]=t[n]
t[n]=a
print(t)
