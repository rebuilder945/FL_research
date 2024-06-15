ls=list(eval(input()))
n,m=eval(input())
tmp=[]
pos_ls=[]
if n>len(ls)-1 and m>len(ls)-1 and n<=m:
    print("error")
else:
    for i in range(n,m):
        tmp.append(ls[i])
    for i in range(len(ls)):
        if ls[i] in tmp:
            continue
        else:
            pos_ls.append(ls[i])
print(pos_ls)

        

