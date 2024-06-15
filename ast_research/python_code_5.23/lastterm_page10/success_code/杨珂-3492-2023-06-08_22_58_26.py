a=str(input())
b=[]
for i in a:
    b.append(i)
if len(a)!=0:
    for i in b:
        b.remove(i)
        if i not in b:
            print(i)
            break   
else:
    print("None")
