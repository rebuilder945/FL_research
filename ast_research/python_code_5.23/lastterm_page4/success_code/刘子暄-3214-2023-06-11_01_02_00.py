a=eval(input())
i=0
b=[]
for x in a:
    if x!=0:
        b.append(x)
    else:
        i+=1
c=b+i*[0]
print(c)



