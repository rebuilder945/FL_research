n,m,l=eval(input())
lst=[n]
num=n
for i in range(m-1):
    num+=l
    lst.append(num)
print(lst)
    
