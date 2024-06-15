nlst = input().split(',')
glst = input().split(',')
dic = {}
for i in range(len(nlst)):
    dic[nlst[i]] = int(glst[i])  # 注意列表索引是用[]而不是()
lst = []
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1])
print(lst)
