int_ls = input().split()
n,m=input().split(",")
if -len(int_ls)<=int(n)<=len(int_ls)-1:
    a=list[n]
    for x in range(int(m)):
        int_ls.append(a)
    print(int_ls)
else:
    print("error")
