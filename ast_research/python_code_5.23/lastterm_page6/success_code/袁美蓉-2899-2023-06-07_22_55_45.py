n,m = int(input())
if m-n >= 3 and m<n and n>=8:
    for a in range(n,m):
        for b in range(n,m):
            for c in range(n,m):
                if a != b and b != c and c != a:
                    s = a*100+b*10+c*1
                    if s >99:
                        print(s,end="") 
else:
    print('illegal input')           



                    




