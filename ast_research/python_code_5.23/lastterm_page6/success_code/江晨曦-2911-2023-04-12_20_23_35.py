#1
a = input()
b = ""
for i in a:
    b = b+str((int(i)+5)%10)
for x in range(len(b)//2):
    b[x]=b[-x-1]
print(int(b))
