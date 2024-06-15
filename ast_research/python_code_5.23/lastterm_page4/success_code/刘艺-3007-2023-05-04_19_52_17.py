list = eval(input())
n , m = eval(input())
if n <= m and m <= len(list)-1:
    for x in range(n,m):
        list.pop(x)
    print(list)
else:
    print("error")

 
