n=eval(input)
x=[m for m in range(1,n+1)]
lst=[]
for i in x:
        if i>=2:
            for j in range(2,i,1):
                if i%j==0:
                    lst.append(i)
for a in range(len(lst)):
    lst[a]=str(lst[a])
lst1=[]
for i in range(len(lst)):
    b=lst[i][::-1]
    lst1.append(b)

