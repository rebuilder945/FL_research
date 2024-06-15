#1
a = input()
b = ""
for i in a:
    b = b+str((int(i)+5)%10)
b.sort()
print(int(b))
