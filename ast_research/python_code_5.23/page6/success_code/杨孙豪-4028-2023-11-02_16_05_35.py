n=eval(input())

lst=[x for x in range(2,n)]
if 0 in lst:
    lst.remove(0)
if 1 in lst:
    lst.remove(1)
result=[]
for i in lst[:]:
    for m in range(2,i):
        if i%m!=0:
            continue
        elif i in lst:
            lst.remove(i)
for i in lst:
    x=str(i)
    b=x[::-1]
    if x!=b:
        lst.remove(i)

bst=list(map(str,lst))
a=' '.join(bst)
print(a)
