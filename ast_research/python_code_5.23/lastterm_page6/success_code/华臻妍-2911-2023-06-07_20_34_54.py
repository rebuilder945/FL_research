num=input()
num1=[]
n=len(num)
for i in num:
    a=(int(i)+5)%10
    num1.append(a)
for i in range(n//2):
    temp=num1[i]
    num1[i]=num1[n-1-i]
    num1[n-1-i]=temp
num1=[str(i) for i in num1]
print(''.join(num1))#‘’用于分隔列表中的元素

