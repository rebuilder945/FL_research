lst=eval(input())
lst.sort(reverse=True)
lst3=[str(x) for x in lst]
strl="".join(lst3)
n=int(strl)
print(n)
