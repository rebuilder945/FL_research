a = input().split()
dict={}
for i in a:
    if i not in dict:
        dict[i] = a.count(i)
max_value= max(list(dict.values()))
save=[]
for i in dict.items():
    if i[1] == max_value:
        save.append(i[0])
save.sort()
for i in save:
    print(i,max_value)

