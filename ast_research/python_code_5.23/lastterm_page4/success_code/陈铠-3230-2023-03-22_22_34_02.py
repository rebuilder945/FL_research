lst=eval(input())
lst.sort()
lst.reverse()
lst1=[str(x) for x in lst]
print("".join(lst1))
