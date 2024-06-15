code = list(input())
if len(code)!= 18:
    print("wrong")
b =[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum = 0
for x in range(17):
    sum+=int(code[x])*b[x]
mod = sum%11
c=[0,1,2,3,4,5,6,7,8,9,10]
d=[1,0,'X',9,8,7,6,5,4,3,2]
g= []
for y in range(11):
    g.append([c[y],d[y]])
for m in g:
    if m[0]==mod and m [1]==code[17]:
        print("correct")
    else:
        print("wrong")
