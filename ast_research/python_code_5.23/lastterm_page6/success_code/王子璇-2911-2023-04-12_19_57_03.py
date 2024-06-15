a=input()
lst=[]
for x in range(len(a)):
    b=(int(a[x])+5)%10
    lst.append(b)
lst.reverse()
print(''.join(str(i)for i in lst))

