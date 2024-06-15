im=input()
n=int(im[0])
m=int(im[2])
coun=0
if n>=m:
    print('illegal input')
elif n<m:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a!=b and b!=c and a!=c:
                    if a!=0:
                        print(a*100+b*10+c,end=' ')
                        coun+=1
    if coun==0:
        print('illegal input')
