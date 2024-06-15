ls=list(eval(input()))
ls.sort(reverse=True)
max=''.join(map(str,ls)) 
print(int(max))
