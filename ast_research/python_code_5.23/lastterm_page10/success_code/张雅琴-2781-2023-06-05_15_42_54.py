a="".join(input())
if len(a)!=18:
    print("Wrong")
else:
    b=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    c=[]
    e=["1","0","X","9","8","7","6","5","4","3","2"]
    for i in range(0,17):
        c.append(int(a[i])*b[i])
d=sum(c)%11
if a[17]==e[d]:
    print("Correct")
else:
    print("Error")


