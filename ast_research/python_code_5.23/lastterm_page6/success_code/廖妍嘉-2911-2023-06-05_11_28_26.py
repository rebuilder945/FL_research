n=list(map(int,input()))
ls=[(x+5)%10 for x in n]
ls.reverse()
b=''.join(str(c) for c in ls)
print(b)
        

