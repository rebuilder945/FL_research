a=list(input())
if len(a)!=0:
    for i in a:
        b=a.count(i)
        if b==1:
            print(i)
            break
else:
    print("None")
 
