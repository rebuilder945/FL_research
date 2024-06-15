m = input()
n = input()
#def color():
lscolor = ["red","blue","yellow"]
secolor = ["purple","orange","green"]
a=-5
b=-5
for x in range(0,3):
    if lscolor[x]==m:
        a = x
for y in range(0,3):
    if lscolor[y]==n:
        b = y
z = a + b -1
if a == b or z<0:
    print("error")
else:
    print(secolor[z])
 
