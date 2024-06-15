dic = {}
x = ""
while x!="q":
    x = input()
    dic[x] = dic.get(x,0)+1
lst = list(dic.items())
lst = sorted(lst,key = lambda x:x[1])
print(*lst[len(lst)-1])
