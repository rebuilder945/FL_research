a=eval(input())
b,c=eval(input())
if 0<=b<len(a) and 0<=c<len(a) and b<c:
    del a[b:c]
elif 0<=b<len(a) and 0<=c<len(a) and b>c:
    del a[c:b]
    print(a)
else :
    print("error")


    




    

