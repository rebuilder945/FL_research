num1 =str(input())
num2=''
for i in num1:
    x = int(i)
    x = (x+5)%10
    num2 = str(x)+num2
print(num2)
