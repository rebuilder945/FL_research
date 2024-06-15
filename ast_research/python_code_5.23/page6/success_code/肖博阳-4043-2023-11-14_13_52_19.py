s=''.join(eval(input()))
for x in  "abcdefghijklmnopqrseuvwxyz":
    if x in s:
        n=s.count(x)
        print(x+","+str(n))
    
