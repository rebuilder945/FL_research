n=eval(input())
lst=[x+1 for x in range(n)]
m=lst.pop(0)
lst.append(m)
print(lst)
