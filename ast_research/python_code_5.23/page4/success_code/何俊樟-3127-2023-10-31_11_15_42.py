a=eval(input())
b=[x for x in range(1,a+1)]
c=0
for x in range(len(b)-1):
    d=b[c]
    e=b[c+1]
    b[0]=e
    b[1]=d
    c+=1
print(b)


