ls1=list(eval(input()))
n,m=eval(input())
if n>=len(ls1) or ((-1)*n)>len(ls1):
     print("Error")
else:
    for i in range(m):
        ls1.append(ls1[n])
    print(ls1)
