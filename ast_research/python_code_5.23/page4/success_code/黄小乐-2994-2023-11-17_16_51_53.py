ls = list(eval(input()))
for i in range(len(ls)):
    if ls.count(ls[i])==len(ls):
        print(ls[i])
        break
    else:
        ls.sort(reverse=True)
        print(ls[i],end="")
        

