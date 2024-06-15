def sux(n):
    List1 = []
    if n<=100:
        return "none"
    elif n<1000:
        List = [int(i) for i in range(100,n+1)]
    elif n>=1000:
        List = [int(i) for i in range(100,1000)]
    for i in List:
        A=str(i)
        if int(A[0])**3 +int(A[1])**3+int(A[2])**3 == int(A):
            List1.append(int(A))
    if List1 == []:
        return "none"
    else:
        return "\n".join(str(i) for i  in List1)
n =eval(input())
print(sux(n))
