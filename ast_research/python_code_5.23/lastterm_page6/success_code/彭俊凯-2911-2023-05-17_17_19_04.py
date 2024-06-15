a=input()
b=[]
for i in range(len(a)):
    b.append((eval(a[i])+5)%10)
b.reverse()
print(''.join(map(str,b)))

