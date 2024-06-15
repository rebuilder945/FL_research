a=eval(input())
b=[]
c=''
for i in a:
    if a.count(i)==1:
        b.append(i)
        b.sort(reverse=False)
        if b==[]:
            b="False"
print(*b,sep=',')  

