a=input()
b=a[-1]
z=0
a=[x for x in a[:-1]]
a=list(map(int,a))
m=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
for i in range(len(m)):
    z+=a[i]*m[i]
z=z%11
if z==2:
    q="X"
else:
    q=(12-z)%11
if str(q)==b:
    print("Correct")
else:
    print("Wrong")
