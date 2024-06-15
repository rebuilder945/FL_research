s=str(input())
zimu=0
shuzi=0
fuhao=0
kongge=0
for i in range(len(s)):
    a=s[0]
    if a in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']:
        zimu+=1
    elif a in ['0','1','2','3','4','5','6','7','8','9']:
        shuzi+=1
    elif a ==' ':
        kongge+=1
    else:
        fuhao+=1
print(zimu,kongge,shuzi,fuhao)

