a=str(input())
b=[]
for i in a:
    b.append(i)
if len(a)!=0:
    for i in range(len(a)):
        b.remove(a[i])
        if a[i] not in b:
            print(a[i])
            break   
else:
    print("None")
