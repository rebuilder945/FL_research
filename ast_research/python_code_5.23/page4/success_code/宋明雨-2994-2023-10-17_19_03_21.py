List = [int(x) for x in input().split(",")]
n,m = eval(input())
if n<= len(List):
    A = List[n]
    for i in range(m):
        List.append(A)
    print(List)
else:
    print("error")


