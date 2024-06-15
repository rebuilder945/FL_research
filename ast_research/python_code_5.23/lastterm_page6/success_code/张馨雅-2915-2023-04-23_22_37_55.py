number = int(input())
flg=0
for i in range(100,number+1):
    s=str(i)
    if int(s[0])**3+int(s[1])**3+int(s[2])**3==i:
        flg+=1
        print(i,end='\n')
if flg==0:
    print('none')
