a=list(input())
f=0
j=0
n=0
m=0
for x in a:
    for i in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
        if x==i:
            f +=1
    if x==" ":
        j +=1
    for i in ['1','2','3','4','5','6','7','8','9','0']:
        if x==i:
            n+=1
    for i in ['!','@','#','%','$','^','&','*','(',')']:
        if x==i:
            m+=1
print(f,j,n,m)




