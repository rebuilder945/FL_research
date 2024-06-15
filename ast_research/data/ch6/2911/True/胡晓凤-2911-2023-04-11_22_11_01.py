a=input()
c=[]
for i in range(len(a)):
    c.append(int(a[i]))
    # 将a中的数字转为列表的形式
for j in range(len(c)):
    c[j]=(c[j]+5)%10
c.reverse()
for k in range(len(c)):
    print(c[k],end='')
