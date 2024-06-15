lst1=input()
lst2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x1 in lst2:
    jishu=0
    for x2 in lst1:
        if x1==x2:
            jishu+=1
    if jishu!=0:
        print("{} {}".format(x1,jishu))
