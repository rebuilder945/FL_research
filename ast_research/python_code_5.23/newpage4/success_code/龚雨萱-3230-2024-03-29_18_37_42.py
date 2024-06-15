ls=list(map(int,input().split(",")))
ls.sort(reverse=True)
max=''.join(map(str,ls)) 
print(int(max))
