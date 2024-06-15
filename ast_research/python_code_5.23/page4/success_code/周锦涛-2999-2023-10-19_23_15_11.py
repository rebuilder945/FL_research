a=input()
b=a.split(" ")
m=eval(input())
n=eval(input())
temp=b[m]
b[m]=b[n]
b[n]=temp
print(b)
