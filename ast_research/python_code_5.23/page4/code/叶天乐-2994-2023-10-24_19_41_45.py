ls1 = list(eval(input()))
n,m = eval(input())
if n >=0 and n <=len(ls1):
    for i in range(m):
    ls1.append(ls1[n])
    print(ls1)
else:
    print("error")
    
