lst=eval(input())
lst.sort()
lst.reverse()
if lst.count(0)==len(lst):
    print(0)
else:
    print(('').join(str(i)for i in lst))
