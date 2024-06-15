a=input()
b=""
for i in a:
    i=str((int(i)+5)%10)
    b+=i
b.reverse()
print(int(b))

