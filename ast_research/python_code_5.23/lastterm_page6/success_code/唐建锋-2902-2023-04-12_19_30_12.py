n=int(input())
lst=[(x+1)/x for x in range(n)]
s=sum(eval(lst))
print("%.4f"%s)
