a=eval(input())
a.sort(reverse=False)
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
if b==[]:
    print("False")
c=[str(x) for x in b]
print(','.join(c))

