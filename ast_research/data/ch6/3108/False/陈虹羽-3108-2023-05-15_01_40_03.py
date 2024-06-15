a=eval(input())
b={}
for i in a:
    for x in i:
            b[x]=b.get(x,0)+1
for i in sorted(b.keys()):
      print(i,b[i])
