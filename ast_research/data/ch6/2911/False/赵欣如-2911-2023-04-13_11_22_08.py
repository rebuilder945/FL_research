a=str(input())
b=0
c=1
for i in a:
    i=(int(i)+5)%10
    b+=i*c
    c=c*10
print(int(b))


