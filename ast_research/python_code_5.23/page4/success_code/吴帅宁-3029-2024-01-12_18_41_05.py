name_ls=list(input().split(","))
score_ls=list(eval(input()))
ls=[]
for i in range(len(name_ls)):
    ls1=[name_ls[i],score_ls[i]]
    ls.append(ls1)
print(ls)

