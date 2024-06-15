xi=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
idcard=list(input())
if len(idcard)!=18:
    print("Error")
    exit()
for k in range(17):
    idcard[k]=int(idcard[k])
result=0
for i in range(0,len(xi)):
    result+=xi[i]*idcard[i]
n=result%11
list=["1","0","X","9","8","7","6","5","4","3","2"]
if idcard[-1]==list[n]:
    print("Correct")
else:
    print("Wrong")

