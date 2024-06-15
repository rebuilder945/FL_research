a = input()
eng = ["a","b","c",'d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
kongge=[" "]
b = 0
c = 0
d = 0
for x in a:
    if x in eng:
        b+=1
    elif x in kongge:
        c+=1
    else:
        d+=1
print (b,c,d)
