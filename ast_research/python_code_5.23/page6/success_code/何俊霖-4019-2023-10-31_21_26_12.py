a = input()
b = ""
for i in range(0,len(a)):
    b+=str((int(a[i])+5)%10)
fir = b[0]
las = b[-1]
c = b[-1]+b[1:-1]+b[0]
print(c)
