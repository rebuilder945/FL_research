lst=eval(input())
lst.reverse()
a=''.join(str(x) for x in lst)
print(int(a))
