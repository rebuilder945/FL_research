ls=[x for x in range(1,eval(input())+1)]
for i in range(0,len(ls)-1):
    ls[i],ls[i+1]=ls[i+1],ls[i]
print(ls)
