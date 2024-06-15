n=eval(input())
ls=[i for i in range(1,n+1)]
tmp=ls[1:n]
tmp.append(ls[0])
print(tmp)
