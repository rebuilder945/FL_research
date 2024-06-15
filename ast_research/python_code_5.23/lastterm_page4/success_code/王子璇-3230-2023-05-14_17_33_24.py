lst=eval(input())
lst.sort(reverse=True)
a=''.join(str(x) for x in lst)
print(int(a))
