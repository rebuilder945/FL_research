lst=eval(input())
lst.sort()
lst.reverse()
lst2=[str(i) for i in lst]
num=''.join(lst2)
print(num)
