list1=list(eval(input()))
a,b=eval(input())
if int(a)>=len(list1):
    print("error")
elif int(a)<len(list1):
    ww=[list1[a]]
    bb=ww*b
    kk=list1+bb
    print(kk)
    
