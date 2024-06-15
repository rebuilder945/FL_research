a= list(input())
q=0
w=0
e=0
r=0
for i in a:
    if i == ' ':
        q+=1
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        w+=1
    if i in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
        e+=1
    else:
        r+=1
print(e,q,w,r)

