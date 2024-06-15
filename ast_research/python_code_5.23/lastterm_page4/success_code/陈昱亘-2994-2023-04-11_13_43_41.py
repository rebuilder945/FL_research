lst=input()
n,m=eval(input())
lst2=lst.split(',')
x=[x for x in range(len(lst2))]
y=[-x-1 for x in range(len(lst2))]
if n in x or n in y:
    lst3=[lst2[n]]*m
    lst2.extend(lst3)
    lst4=list(map(int,lst2))
    print(lst4)
else: print('error')
