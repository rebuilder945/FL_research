list=list(input())
if input=="":
    print("None")
l=[]
if input!="":
    for i in list:
        n=list.count(i)
        if n==1:
            l.append(i)
        if not l:
            print("None")
    print(l[0])
