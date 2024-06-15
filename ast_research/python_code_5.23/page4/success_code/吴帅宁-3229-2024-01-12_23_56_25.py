n=eval(input())
ls=[]
tmp=[]
post_ls=[]
for i in range(len(n)):
    if n[i] not in ls:
        ls.append(n[i])
    else:
        tmp.append(n[i])
for i in ls:
      if i not in tmp:
        post_ls.append(i)
post_ls.sort()
if post_ls==[]:
    print("False")
else:
    print(post_ls)
