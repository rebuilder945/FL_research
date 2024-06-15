l=list(input())
m=[]
for i in l:
    i=(int(i)+5)%10
    m.append(i)
m=m[::-1]
print(''.join(str(x)for x in m))





