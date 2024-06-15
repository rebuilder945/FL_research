dic = {}
while True:
    s = input()
    if s == 'q':
        break  
    dic[s] = dic.get(s,0) + 1

lst = list(dic.values())
a = max(lst)

for k,v in dic.items():
    if v == a:
        print(k,v)
