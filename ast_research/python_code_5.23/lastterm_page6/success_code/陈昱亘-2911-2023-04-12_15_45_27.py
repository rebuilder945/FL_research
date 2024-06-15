m=input()
str1=''
for i in range(len(m)):
    a=int(m)%10
    b=(a+5)%10
    str1+=str(b)
    m=str(int(m)//10)
    a=0
print(str1)
