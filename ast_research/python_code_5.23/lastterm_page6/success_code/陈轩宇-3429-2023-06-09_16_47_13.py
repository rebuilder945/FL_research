a = input()
a = list(a)
b = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
c = 0
f = 0
j = 0
d = ['1','2','3','4','5','6','7','8','9']
for i in b:
    for x in a:
        if i==x:
            c+=1
for e in a:
    if e==" ":
        f+=1
for g in d:
    for h in a:
        if g==h:
            j+=1
v = len(a)
v = int(v)
z = v-c-f-j
print("%d %d %d %d"%(c,f,j,z))
    

        
