x = input()
if int(x)<=1 or int(x)!=float(x):
    print("illegal input")
else:
    x=int(x)
    lst2=[]
    lst1=[n for n in range(2,x)]
    for num in lst1:
        for t in range(2,num):
            if x%t==0:
                lst2.append(num)
    end=[]
    for N in lst2:
        if str(N)[::-1]==str(N):
            end.append(N)
    for xnum in end:
        print(xnum,end=" ")
