a=input().split(" ")
a=list(map(int,a))
n=a[0]
m=a[1]

def dummy(n,m):
    lst1=[]
    lst2=[]
    for i in range(n,m):
        lst1.append(i)
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i!=0:
                    sum=100*i+10*j+k
                    lst2.append(sum)
    lst3=lst2.copy()
    for i in range(0,len(lst2)):
        for j in range(n,m):
            if str(lst2[i]).count(str(j))>1:
                lst3.remove(lst2[i])
    if n>=m or lst3==[] or n<0 or m>9:
        print("illegal input")
    else:
        print(" ".join(str(i) for i in lst3))

dummy(n,m)

