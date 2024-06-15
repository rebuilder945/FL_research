
ls=input().split(',')
n,m=input().split(',')
ls2=[]
n=int(n)
m=int(m) and m>0
for i in range(len(ls)):
    ls2.append(int(ls[i]))
if n not in range(-len(ls),len(ls)+1):
    print("error")
else:
    for i in range(m):
        ls2.append(int(ls[n]))
print(ls2)

