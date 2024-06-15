a=list(input())
c=a.copy()
b=len(a)
num1=ord('A')
num2=ord('a')
for i in range(b):
    if a[i].islower():
        a[i]=chr(26-(ord(a[i])-num2)+num2-1)
    elif a[i].isupper():
        a[i]=chr(26-(ord(a[i])-num1)+num1-1)

print(''.join(c))
print(''.join(a))
