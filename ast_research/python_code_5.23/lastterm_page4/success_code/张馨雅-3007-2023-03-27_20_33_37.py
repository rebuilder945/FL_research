Li=eval(input())
n,m=eval(input())
if m<len(Li) and n<len(Li):
    index_list = []
    for i in range(len(Li)):
        if i>=n and i<m:
            index_list.append(i)
    for i in index_list:
        del Li[i]
else:
    print('error')
print(Li)








