num1=eval(input())
num2=[]
for x in num1:
    if num1.count(x)==1:
        num2.append(x)
num2.sort()
if num2==set():
    print(False)
else:
    str1=",".join(map(str,num2))
    print(str1)



