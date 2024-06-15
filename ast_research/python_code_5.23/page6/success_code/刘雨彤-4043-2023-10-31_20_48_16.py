lst1=input()
lst2=["a","b",'c',"d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
for i in lst2:
    jishu=0
    for j in lst1:
        if i==j:
            jishu+=1
    if jishu!=0:
        print("%a,%d"%(i,jishu))
