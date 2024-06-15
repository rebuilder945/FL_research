name = list(input().split(','))
mark = eval(input())
lst = [[name[x],mark[x]] for x in range(len(name))]
print(lst)

