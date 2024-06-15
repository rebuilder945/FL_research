num=eval(input())
count=0
if len(str(num))>3:
    num=999
for x in range(100,num+1):
    num1=str(x)
    sum=(int(num1[0]))**3+(int(num1[1]))**3+(int(num1[2]))**3
    if sum==x:
        count=1
        print(x)
if count==0:
    print("none")

