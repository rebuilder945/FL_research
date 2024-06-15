list=list(input())
if input=="":
    print("None")
l=[]
if input!="":
    for i in list:
        n=list.count(i)
        while n==1:
            l.append(i)
        else:
            print("None")
    print(l[0])
