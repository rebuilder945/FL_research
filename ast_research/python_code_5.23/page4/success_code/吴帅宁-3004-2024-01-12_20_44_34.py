ls=eval(input())
prime_ls=[]
for i in ls:
    if i>=2:
        for m in range(2,i):
            if i%m==0:
                break
        else:
               prime_ls.append(i)
print(prime_ls)

