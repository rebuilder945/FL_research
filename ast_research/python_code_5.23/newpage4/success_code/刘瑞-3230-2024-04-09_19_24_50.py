aug=eval(input())
aug.sort(reverse=True)
a=""
for x in aug:
   a+= str(x)
print(int(a),end="")
