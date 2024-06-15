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

count_lst.sort(key = lambda x:x[1])
max = count_lst[0]



