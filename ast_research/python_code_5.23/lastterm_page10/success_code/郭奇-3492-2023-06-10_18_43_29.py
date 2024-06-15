a=input()

n=0
for i in a[0:]:
    for j in a[n+1:]:
        if i==j:
            del(a[j])
    n+=1
print(a[0])
    


