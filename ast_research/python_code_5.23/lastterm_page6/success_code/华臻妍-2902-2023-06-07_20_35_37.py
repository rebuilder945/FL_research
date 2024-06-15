n=eval(input())
a=1
b=2
sum=0
for i in range(n):
    c=b/a  
    sum=sum+c
    temp=b 
    b=a+b
    a=temp#实现a值的变化
print('%.4f'%sum)

