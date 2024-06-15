s = input()
dic = {}
while s!='q':
    dic[s] = dic.get(s,0)+1
    s = input()
for key,value in dic.items():
    if value == max(dic.values()):
        print(key,value)
