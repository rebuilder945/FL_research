m=eval(input())
n=[]
for i in m:
    l=[range(2,i)]
    for x in l:
        if i%x==0:
            n.append(i)
print(n)
 

