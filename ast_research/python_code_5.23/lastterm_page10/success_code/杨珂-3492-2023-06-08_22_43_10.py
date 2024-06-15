a=str(input())
if len(a)!=0:
    ls=[a[0]]
    for i in a:
        if i not in ls:
            print(i)
            break   
else:
    print("None")
