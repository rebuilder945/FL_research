list_input = input().split(",")
n,m = eval(input())


lists = list(map(int, list_input))

if(n>=len(lists)):
    print("error")
else:
    num = lists[n]
    for i in range(m):
        lists.append(num)
    print(lists)
