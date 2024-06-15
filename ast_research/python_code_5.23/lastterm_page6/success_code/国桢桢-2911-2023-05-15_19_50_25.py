l = list(map(int,str(input())))
for i in range(len(l)):
    l[i]=(l[i]+5)%10
l1=l[::-1]
a = ''.join(map(str,l1))
print(a)
