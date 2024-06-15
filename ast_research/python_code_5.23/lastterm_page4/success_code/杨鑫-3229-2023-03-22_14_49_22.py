lst = eval(input())
A = []
for i in lst:
    a = lst.count(i)
    if a==1:
        A.append(i)
if A==[]:
    print(False)
else:
    A.sort()
    print(','.join(map(str,A)))
