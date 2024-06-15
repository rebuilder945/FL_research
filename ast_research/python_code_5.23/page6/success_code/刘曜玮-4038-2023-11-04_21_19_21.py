a = input()
eng = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kongge=[" "]
shuzi = ['0','1','2','3','4','5','6','7','8','9']
b = 0
c = 0
d = 0
f = 0
for x in a:
    if x.isalpha():
        b+=1
    elif x in kongge:
        c+=1
    elif x in shuzi:
        f+=1
    else:
        d+=1
print (b,c,f,d)
