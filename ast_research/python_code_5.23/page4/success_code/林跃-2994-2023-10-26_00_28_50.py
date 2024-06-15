lst=list(eval(input()))
n,m=eval(input())
if n<len(lst) and n>=(-len(lst)):
    for i in range(m):
        lst.append(lst[n])
    print(lst)
else:
    print('error')
