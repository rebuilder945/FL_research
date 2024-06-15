def hanshu(a):
    lst2=[]
    lst=[int(x) for x in str(a)]
    for i in lst:
        lst2.append(i**3)
    if sum(lst2)==a:
        return a
n=eval(input())
lst3=[]
for i in range(2,n):
    if hanshu(i)==i:
        lst3.append(i)
        if lst3==[]:
            print("none")
        else:
            print(i)

