lst1=eval(input())
lst2=[]
for x in lst1:
    for i in range(2,x):
        if x%i!=0:
            lst2=[x]
            print(lst2)
