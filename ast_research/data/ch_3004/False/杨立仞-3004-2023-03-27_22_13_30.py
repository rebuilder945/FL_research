a=eval(input())
new=[]
for i in range(len(a)):
    b=[i%x for x in range(1,i)]
    if b.count(0)==1: 
        new.append(i)
print(new)
