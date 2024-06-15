x=input()
y=""
for i in x:
    q=(int(i)+5)%10
    y=str(q)+y
print(y)

