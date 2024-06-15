def hanshu(a):
    lst2=[]
    lst=[int(x) for x in str(a)]
    for i in lst:
        lst2.append(i**3)
    if sum(lst2)==a:
        return a
n=eval(input())
for i in range(n):
    if hanshu(i)==i:
        print(i)

