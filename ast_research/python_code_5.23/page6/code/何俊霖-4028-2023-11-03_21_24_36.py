x = input()
if x<=1 or int(x)!=float(x):
    print("illegal input")
else:
    lst2=[]
    lst1=[n for n in range(2,x)]
    for num in x:
        for t in range(2,num):
            if x%t==0:
                lst2.append(num)
    e=[i for i in lst1 if i not in lst2]
    end=[]
    for N in e:
        if str(N)
