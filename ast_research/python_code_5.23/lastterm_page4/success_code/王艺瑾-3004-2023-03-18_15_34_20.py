x=eval(input())
a=[]
for i in x:
    if i>=2:
        for j in range(2,i,1):
            if i%j==0:
                break
        else:a.append(i)
print(a)
