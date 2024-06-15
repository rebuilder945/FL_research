n=eval(input())
list2=[]
list3=[]
if n<=1:
    print("illegal input")
else:
    list1=[x for x in range(1,n+1)]
    for i in list1:
        m=0
        for y in range(1,i):
            if i%y!=0:
                m=m+1
            if m==i-1:
                list2.append(i)
    for j in list2:
        r=1
        for k in range(len(list(j)//2)):
            if(list(j)[k]!=list(j)[-k-1]):
                r=0
                break
            if r==0:
                list3.append(list(j))
        for l in list3:
            print(l,end="")
