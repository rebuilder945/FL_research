List = eval(input())
a,b =eval(input())
m = max(a,b)
n = min(a,b)
if m > len(List):
    print("error")
else:
    del List[n:m]
    print(List) 
