def ave(x):
    d = sum(x)/len(x)
    if int(d) == d:
        return(int(d))
    else:
        return("%.2f"%(d))
a = eval(input())
print(ave(a))
