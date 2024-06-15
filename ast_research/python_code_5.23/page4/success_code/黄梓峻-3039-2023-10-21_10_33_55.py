lst=eval(input())
if len(lst)>2:
    lst.remove(max(lst))
    lst.remove(min(lst))
    print(lst)
else:
    print("[]")
