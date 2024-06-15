m=input()
a=0
b=0
c=0
d=0
for x in m:
    if x in ['1','2','3','4','5','6','7','8','9']:
        c+=1
    elif x==" ":
        b+=1
    elif x in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        a+=1
    else:
        d+=1
print(a,b,c,d)
