m = input()
n = input()
#def color():
lscolor = ["red","blue","yellow"]
secolor = ["purple","orange","green"]
a=0
b=1
for x in range(0,3):
    if m==lscolor[x]:
        a = x
for y in range(0,3):
    if n==lscolor[y]:
        b = y
z = a + b
if a == b:
    print("error")
else:
    print(secolor[z])
 
