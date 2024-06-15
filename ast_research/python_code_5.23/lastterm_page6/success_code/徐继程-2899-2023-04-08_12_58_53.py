im=input()
n=int(im[0])
m=int(im[2])
coun=0
if n>=m:
    print('illegal input')
elif n<m:
    for a in range(n,m+1):
        for b in range(n,m+1):
            for c in range(n,m+1):
                if a!=b and b!=c and a!=c:
                    print(a*100+b*10+c,end=' ')
                    coun+=1
    if coun==0:
        print('illegal input')
