a=eval(input())
b=0
c=0
while a!='#':
        b+=1
        c+=eval(a)
        a=input()
print(b%c)
