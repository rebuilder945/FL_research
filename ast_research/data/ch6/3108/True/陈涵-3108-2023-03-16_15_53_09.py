n=eval(input())
n="".join(n)
for i in ["a","b","c","d","e","f","g","h","i",'j',"k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
    if n.count(i)!=0:
        print("%s,%d"%(i,n.count(i)))
    else:
        pass    
