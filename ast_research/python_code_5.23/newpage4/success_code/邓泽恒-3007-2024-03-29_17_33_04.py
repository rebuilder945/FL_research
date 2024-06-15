a=eval(input())
n,m=eval(input())
if n not in a or m not in a:
    print(error)
else:
    for x in a:
        if x>=n and x<m:
            a.remove(x)
print(a)

    
