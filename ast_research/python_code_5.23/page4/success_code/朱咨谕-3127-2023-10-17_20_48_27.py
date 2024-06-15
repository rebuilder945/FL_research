a=eval(input())
ls=[]
for i in range(1,a+1):
    ls.append(i)
for i in range(1,a):
    ls[i-1]=ls[i]
ls[a-1]=1
print(ls)


