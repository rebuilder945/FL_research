num=eval(input())
lst=list(map(int,str(num)))
x=[]
for i in lst:
    a=(i+5)%10
    x.append(a)
x.reverse()
num2=map(str,x)
num1="".join(num2)
print(num1)
