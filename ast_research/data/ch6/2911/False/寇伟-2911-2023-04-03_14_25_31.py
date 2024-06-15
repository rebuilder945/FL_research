num = input()
num1=''
for i in num:
    i = int(i)
    i=(i+5)%10
    num1+=str(i)
num1=num1[:]
print(num1)






