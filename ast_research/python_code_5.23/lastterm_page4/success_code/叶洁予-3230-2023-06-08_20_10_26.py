lst=eval(input())
lst.sort(reverse=True)
lst1=[str(x) for x in lst]
s="".join(lst1)
n=int(s)
print(s)

