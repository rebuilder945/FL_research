a = input() or 'q'
dic ={}
while a != 'q':
    if a not in dic:
        dic[a]=1
    elif a in dic:
        dic[a] +=1
    a = input() or 'q'
lst = list(dic.values())
b = max(lst)
for x in dic:
    if dic[x]==b:
        print(x,b)



