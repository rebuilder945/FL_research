n = eval(input())
list = list(range(1,n+1))
re_list = []
for i in range(1,n):
    re_list.append(list[i])
re_list.append(list[0])
print(re_list)
