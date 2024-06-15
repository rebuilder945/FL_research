lst=list(input())
zifu=list("!@#$$%^")
shuzi=list("1234567890")
zifushu=0
shuzishu=0
konggeshu=0
zimu=0
for x in lst:
    if x in zifu :
        zifushu+=1
    elif x in shuzi:
        shuzishu+=1
    elif x ==" ":
        konggeshu+=1
    else:
        zimu+=1
print(zimu,konggeshu,shuzishu,zifushu)

