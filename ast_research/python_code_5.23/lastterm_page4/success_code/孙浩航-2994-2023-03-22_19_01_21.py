list1=list(eval(input()))
a,b=eval(input())
if b>len(list1)+1:
    print("error")
elif b<=len(list1)+1:
    ww=[list1[a]]
    bb=ww*b
    kk=list1+bb
    print(kk)

