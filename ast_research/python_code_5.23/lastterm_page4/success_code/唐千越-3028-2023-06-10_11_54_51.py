n,m,l = map(int,input().split(','))
lst = [n]
if m-1>0:
    n += l
    lst.append(n)
    m -= 1
print(lst)



