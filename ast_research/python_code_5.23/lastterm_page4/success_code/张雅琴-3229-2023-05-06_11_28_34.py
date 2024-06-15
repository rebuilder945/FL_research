a=eval(input())
b=[]
c=0
for i in a:
    if a.count(i)==1:
        c+=1
        b.append(i)
    print(map(int,b))
    if c==0:
        print("False")
