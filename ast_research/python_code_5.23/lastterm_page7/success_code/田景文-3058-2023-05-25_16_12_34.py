dic = {}
x = input()
while x != 'q':
    dic[x] = dic.get(x,0) + 1
    x = input()
#print(max(dic,key=dic.get),end=' ')
#print(max(dic.values()))
s = 0
for i in dic.values():
    if i > s:
        s = i
for x in dic.keys():
    if dic[x] == s:
        print(f"{x} {s}")
