a=list(input())
b=0
c=0
d=0
f=0
for i in range(len(a)):
    if a[i] in ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
        b+=1
    elif a[i] in map(str,[1,2,3,4,5,6,7,8,9,0]):
        c+=1
    elif a[i] == ' ':
        d+=1
    else:
        f+=1
print(b,c,d,f)

