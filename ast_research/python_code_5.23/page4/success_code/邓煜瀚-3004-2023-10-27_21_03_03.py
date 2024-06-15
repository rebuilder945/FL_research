a=eval(input())
b=[]
for i in a:
    if a.count(i)==1:
        b.append(i)
    elif a.count(i)==0:
        print("False")
b.sort()
print(b)




