x = input()
if "." in x:
    print("illegal input")
elif int(x)>0 and float(x)!=int(x):
    x=int(x)
    lst2=[]
    lst1=[n for n in range(2,x)]
    for num in lst1:
        for t in range(2,num):
             if num%t==0 and num not in lst2:   #lst2是合数
                lst2.append(num)
    end=[N for N in lst1 if N not in lst2]
    for N in end:
        if str(N)[::-1]==str(N):
            print(N,end=" ")
else:
    print("illegal input")

