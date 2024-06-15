lst=eval(input())
r=input()
a,b=eval(r)
num=len(lst)
hi="nihao"
if b<=num-1 and a>=0:
    for x in range(a,b):
        lst[x]=hi
    while hi in lst:
        lst.remove(hi)
    print(lst)
else:
    print("error")
