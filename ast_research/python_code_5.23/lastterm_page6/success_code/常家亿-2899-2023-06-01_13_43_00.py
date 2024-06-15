n,m = map(int,input().split())#空格隔开输入
str1 = ''
lst = []
if m - n==3:
    for i in range(n,m):
        for j in range(n,m):
            for k in range(n,m):
                if i != j and k!=i and k!=j:
                    if str(i) != '0':
                        str1 = str(i)+str(j)+str(k)
                        lst.append(str1)
    print(' '.join(lst))   
else:
    print('illegal input')



