a=input()
a=list(a)
n=0
if a==[]:
    print("None")
else:
    for i in a[0:]:
        for j in a[n+1:]:
            if i==j:
                del(j)
        n+=1
    print(a[0])
    


