
lst=eval(input())
lst.sort(reverse=True)
lst2=[str(x)for x in lst]
str1="".join(lst2)
n=int(str1)
print(n)
