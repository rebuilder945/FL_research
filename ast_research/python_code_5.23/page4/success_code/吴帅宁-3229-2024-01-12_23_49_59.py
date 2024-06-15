n=eval(input())
ls=[]
tmp=[]
post_ls=[]
for i in n:
    if n.count(i)!=1:
        print("False")
        break
    else:
        for i in range(len(n)):
         if n[i] not in ls:
           ls.append(n[i])
        else:
          tmp.append(n[i])
    for i in ls:
      if i not in tmp:
        post_ls.append(i)
    post_ls.sort()
    print(post_ls)
