a = list(input())
c = ""
for i in a[::-1]:
    b = (int(i)+5)%10
    c+=str(b)

print(c)
    
