lst=list(eval(input()))
n,m=eval(input())
d=[]
if (n+1)<=len(lst):
    for x in range(m ):
        d.append(lst[n])
    lst=lst+d
    print(lst)
else:
    print('error')
