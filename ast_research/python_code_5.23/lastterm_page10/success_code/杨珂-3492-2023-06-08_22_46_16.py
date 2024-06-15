a=str(input())
b=a.split("")
if len(a)!=0:
    for i in a:
        if i not in b.remove(i):
            print(i)
            break   
else:
    print("None")
