lst=eval(input())
r=input()
a,b=eval(r)
num=len(lst)
if b<=num-1 and a>=0:
    for x in range(a,b):
        lst[x]="k"
    while "k" in lst:
        lst.remove("k")
else:
    print("error")
