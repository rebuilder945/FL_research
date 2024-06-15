#heart和earth是变位词，Mary和arMy也是
m=list(input()) 
n=list(input())
l=len(m)
g=len(n) 
f=0
if l==g:
    if l == 1 and m == n:      #要考虑到和原来的是不是重复了，但是a和a同样都是变位词
        print("yes")
    elif m == n and l != 1:
        print("no")
    elif l == 1 and m != n:
        print("no")
    else:
        for i in range(l):
            if m[i] in n:
                continue 
            else:
                f+=1        
                break
        if f==0:
            print("yes") 
        else:
            print("no")
else:
    print("no")
