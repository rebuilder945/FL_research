ls = eval(input())
ls.sort()
ls.reverse()
for i in ls:
    if i ==0:
        print("0")
    else:
        print(*ls,sep='')    
