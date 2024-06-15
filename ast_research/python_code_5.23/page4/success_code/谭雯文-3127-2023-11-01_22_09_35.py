n1=[x for x in range(1,5)]
for i in range(len(n1)-1):
    n1[i],n1[i+1]=n1[i+1],n1[i]
print(n1)
