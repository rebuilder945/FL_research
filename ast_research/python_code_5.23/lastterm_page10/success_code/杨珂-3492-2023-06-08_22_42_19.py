a=str(input())
if a!=None:
    ls=[a[0]]
    for i in a:
        if i not in ls:
            print(i)
            break   
else:
    print("None")
