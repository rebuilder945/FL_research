n,m,l = map(int,input().split(','))
lst = [n]
while m-1>0:
    n += l
    lst.append(n)
    m -= 1
print(lst)



