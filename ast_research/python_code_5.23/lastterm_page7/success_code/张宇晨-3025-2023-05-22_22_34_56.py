st = list(input().split(" "))

dic = {}

for i in st:
    dic[i] = dic.get(i,0)+1
lst = sorted(list(dic.items()),key = lambda x:(-x[1],x[0]),reverse=True)
x = len(lst)-1
while lst[x][1]==lst[len(lst)-1][1] :
    print(*lst[x])
    if x>0:
        x -=1
    else:
        break
