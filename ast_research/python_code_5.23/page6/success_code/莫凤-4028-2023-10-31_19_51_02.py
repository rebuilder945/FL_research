n=eval(input())
if n>1 and isinstance(n,int):
    list2=[]
    for x in range(2,n):
        if x>=2:
            num = 2
            for y in range(2,x,1):
                if x%y==0:
                    break            
                num += 1
            if num == x:
                list2.append(x)
    list3=[x]
    for x in range(2,n):
        if str(x)==str(x)[::-1]:
            list3.append(x)
    print(list3)
    print(list2)
    for x in range(2,n):
        if x in list2 and x in list3:
            print(x,end=" ")
else:
    print("illegal input")

