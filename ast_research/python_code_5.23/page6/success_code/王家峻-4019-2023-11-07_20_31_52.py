c=list(input())
w=''
for i in c:
    w+=str((int(i)+5)%10)
print(w[::-1])


