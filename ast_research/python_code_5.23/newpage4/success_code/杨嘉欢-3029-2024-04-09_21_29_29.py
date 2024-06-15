a=list(map(str, input().split(",")))
b=input()
b=b[1:-1]
b=list(map(int, b.split(",")))
result=[[a[i],b[i]] for i in range(len(b))]
print(result)
