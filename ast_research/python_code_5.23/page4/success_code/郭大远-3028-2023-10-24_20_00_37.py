n,m,l=eval(input())
c=[]
c.append(n)
for i in range (m-1): 
    n+=l
    c.append(n)
print(list(c))
    



