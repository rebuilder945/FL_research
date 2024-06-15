lst=eval(input())
a,b=input().split(",")
lst=list(lst)
a=int(a)
b=int(b)
if a<=len(lst):
    c=lst[a]
    for x in range(b):
        lst.append(c)
    print(lst)
else:
    print('error')
