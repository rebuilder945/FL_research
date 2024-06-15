lst=eval(input())
lst.sort()
lst.reverse()
lst1=[str(x) for x in lst]
a="".join(lst1)
print(int(a))
