n=int(input())
ls=[]
for i in range(n+1):
    if len(str(n))==3:
        s=str(i)
        a=int(s[0])**3+int(s[1])**3+int(s[2])**3
        if i==a:
            print(i)
            ls.append(i)
if len(ls) == 0:
    print('none')
