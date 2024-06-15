n,m,l = eval(input())
lst=[n]
a=0
while a<m-1:
    x = n+l+l*a
    lst.append(x)
    a+=1
print(lst)
