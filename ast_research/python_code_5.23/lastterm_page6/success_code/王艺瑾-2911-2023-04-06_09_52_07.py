a=eval(input())
b=""
for i in a:
    b=str((int(i)+5)%10)+b
print(b)
