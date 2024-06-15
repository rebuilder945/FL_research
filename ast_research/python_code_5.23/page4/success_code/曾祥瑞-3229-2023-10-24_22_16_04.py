a=eval(input())
a.sort(reverse=True)
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
    else:
        print("False")
c=[str(x) for x in b]
print(','.join(c))
