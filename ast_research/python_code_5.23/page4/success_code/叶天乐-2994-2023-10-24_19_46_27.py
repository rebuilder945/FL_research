ls1 = list(eval(input()))
n,m = eval(input())
if n >=0 and n <=len(ls1):
    for i in range(m):
       ls2 = ls1.append(ls1[n])
       print(ls2)
else:
    print("error")
