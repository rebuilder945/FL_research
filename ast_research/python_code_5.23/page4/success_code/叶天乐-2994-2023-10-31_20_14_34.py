ls1 = list(eval(input()))
n,m = eval(input())
if n>len(ls1)-1:
    print("error")
elif n>0 and n<=len(ls1)-1:
    for i in range(m):
        ls1.append(ls1[n])
    print(ls1)
else:
    n = n+len(ls1)
    for i in range(m):
        ls1.append(ls1[n])
    print(ls1)
    


