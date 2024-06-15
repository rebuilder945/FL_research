a = (input())
b = 0
for i in range(len(a)):
    b += ((int(a[i])+5)%10)*(10**i)
if a[-1] == '5':
    c = '0'+str(b)
    print(c)
else:
    print(b)


