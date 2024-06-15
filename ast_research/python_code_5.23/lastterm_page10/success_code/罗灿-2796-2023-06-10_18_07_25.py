s=input()
ls=[]
n=0
st=''
for i in s:
    if i.isdigit():
        n+=1
        st+=i
    else:
        ls.append(st)
        st=''
    ls.append(st)
if n==0:
    print('No digits')
else:
    if len(ls)==1:
        print(ls[0])
    else:
        ls1=[]
        for x in ls:
            n=len(x)
            ls1.append(n)
        for y in range(len(ls)-1,-1,-1):
            if len(ls[y])==max(ls1):
                print(ls[y])
                break
