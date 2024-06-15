lst=list(input())
zimu=list("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLXCVBNM")
shuzi=list("1234567890")
zifushu=0
shuzishu=0
konggeshu=0
zimushu=0
for x in lst:
    if x in zimu :
        zimushu+=1
    elif x in shuzi:
        shuzishu+=1
    elif x ==" ":
        konggeshu+=1
    else:
        zifushu+=1
print(zimushu,konggeshu,shuzishu,zifushu)

