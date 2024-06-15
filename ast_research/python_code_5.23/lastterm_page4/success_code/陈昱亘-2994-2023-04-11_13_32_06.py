lst=input()
n,m=eval(input())
lst2=lst.split(',')
if n in [x for x in range(len(lst2))]:
    lst3=[lst2[n]]*m
    lst2.extend(lst3)
    lst4=list(map(int,lst2))
    print(lst4)
else: print('error')
