a=eval(input())
b="".join(a)
c=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
d=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in b:
    d[c.index(i)]+=1
for x in range(0,26):
    if d[x]!=0:
        print("%s,%d"%(c[x],d[x]))
