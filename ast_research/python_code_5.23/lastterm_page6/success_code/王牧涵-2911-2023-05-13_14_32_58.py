sums=input()
c=[]
for i in range(len(sums)):
    c.append(int(sums[i]))
for j in range(len(c)):
    c[j]=(c[j]+5)%10
c.reverse()
print(''.join(map(str,c)))


