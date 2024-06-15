n=input()
a=''
for i in n:
    i=(int(i)+5)%10
    a=a+str(i)
b=''
for x in range(len(a)):
    b=b+str(a[-1-x])
print(b)
