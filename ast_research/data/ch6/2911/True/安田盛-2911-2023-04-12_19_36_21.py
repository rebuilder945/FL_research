a=input()
b=[]
for i in a:
    b.append(str((int(i)+5)%10))
b.reverse()
n=''
for i in b:
    n+=i
print(n)




