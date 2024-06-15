a=str(input())
b=[]
for i in a:
    b.append(i)
if len(a)!=0:
    for i in a:
        if i not in b.remove(i):
            print(i)
            break   
else:
    print("None")
