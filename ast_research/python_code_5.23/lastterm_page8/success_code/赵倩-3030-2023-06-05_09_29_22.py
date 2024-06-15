a=input().split(",")
b=input().split(",")
list=[]
if len(a)!=0:
    for i in range(len(a)):
        list.append([a[0],int(b[0])])
        del a[0]
        del b[0]
    print(list)

        

       



                    




