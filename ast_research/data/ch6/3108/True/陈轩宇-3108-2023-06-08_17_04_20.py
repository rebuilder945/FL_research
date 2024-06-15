a = input()
a = list(a)
b=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in b:
    x=0
    for j in a:
        if i == j:
            x=x+1
    if x!=0:
        print("%c,%d"%(i,x))

    



    
