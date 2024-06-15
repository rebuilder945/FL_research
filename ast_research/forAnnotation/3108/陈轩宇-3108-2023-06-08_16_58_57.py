a = input()
a = list(a)
b=["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k“,”l“,”z“,”x“,”c“,”b“,”n“,”m"]
for i in b:
    x=0
    for j in a:
        if i == j:
            x=x+1
    if x!=0:
        print("%c,%d"%(i,x))

    



    
