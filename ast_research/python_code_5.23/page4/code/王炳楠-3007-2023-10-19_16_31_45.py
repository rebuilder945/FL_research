lie=eval(input())
a=len(lie)
n,m=eval(input())
if n>a-1 or m>a-1:
    print("error")
else:
    if n<m:
        for i in range(n,m):
            del lie[i]
        print(lie)
    elif n>m:
        for i in range(n,m,-1)
            del lie[i]
        print(lie)
        
            
