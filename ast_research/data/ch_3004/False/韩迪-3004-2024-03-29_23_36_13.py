a=list(eval(input()))
upper=max(a)
lower=min(a)
list=[]
i=2
for i in range(lower,upper):
    j=2
    for j in range(2,i):
        if i%j==0:
            break
        else:
            list.append(i)
print(list)
