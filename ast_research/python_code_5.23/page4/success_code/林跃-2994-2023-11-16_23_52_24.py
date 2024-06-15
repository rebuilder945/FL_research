lst=list(eval(input()))
n,m=eval(input())
lst1=lst.copy()
if n<=len(lst) and n>=(-len(lst)):
    for i in range(m):
        lst1.append(lst[n])
    print(lst1)
else:
    print('error')

