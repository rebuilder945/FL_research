list1=list(input().split())
d={}
for i in list1:
    if i!="q":
        m=n=list1.count(i)
        while m>1:
            list1.remove(i)
            m-=1
        print(i,n)    
