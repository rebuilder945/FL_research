from re import M


a=eval(input())
b,c=eval(input())
if b>len(a)-1 or c>len(a)-1:
    print("error")
else :
    if b<c:
        del a[b:c]
    else:
        del a[b:c:-1]
    print(a)
    


    




    

