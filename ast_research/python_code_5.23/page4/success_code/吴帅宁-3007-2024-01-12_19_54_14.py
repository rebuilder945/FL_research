ls=list(eval(input()))
n,m=eval(input())
tmp=[]
pos_ls=[]
if n>len(ls) and m>len(ls):
    print("error")

elif n>m or n<0:
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


