a,b,c,d=input().split()

ave=(eval(b)+eval(c)+eval(d))/3
e=[eval(b),eval(c),eval(d)]
e.sort(reverse=True)
print("{} {:.2f} {:.2f} {:.2f} {:.2f}".format(a,e[0],e[1],e[2],ave) )
