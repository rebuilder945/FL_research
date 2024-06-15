count = {}
s = input().split()
for i in s:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

count_lst = []
for k, v in count.items():
    count_lst.append([k,v])

count_lst.sort(key = lambda x:x[1],reverse = True)
max = count_lst[0][1]

max_dic = {}
for a,b in count.items():
    if b == max:
        max_dic[a] = b
max_lst = list(max_dic)
for c in max_lst:
    print('{},{}',format(c[0],c[1]))


