list_input = input().split(",")
n,m = eval(input())


lists = list(map(int, list_input))

if(n<0 or n>=len(lists)):
    print("error")
else:
    for i in range(m):
        lists.append(lists[n])
    print(lists)
