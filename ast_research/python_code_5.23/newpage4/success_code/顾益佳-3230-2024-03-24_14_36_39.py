s = eval(input())
m = list (s)
m.sort(reverse = True)
for x in m :
    if x==0:
        print (x)
        break
    else:
        print (x ,end = "")

    
