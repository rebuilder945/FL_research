namel=list(input().split(","))
scorel=list(map(int,input().split(",")))
print(list(map(list,zip(namel,scorel))).sort(key=lambda criteria:criteria[1],reverse=False))

