n=eval(input())
lst1=[]
lst2=[]
lst3=[]
lst4=[]
if n<=1 or type(n)==float:
    print("illegal input")
else:
    for i in range(2,n+1):
        for x in range(2,i):
            if i%x==0:
                break
        else:
            lst1.append(i)
    for q in lst1:
        m=str(q)
        if m==m[::-1]:
            lst4.append(q)
for p in lst4:
    print(p,end=' ')

