n = input()
s =""
for x in n:
    s +=str((int(x)+5)%10)
print(s[::-1])
