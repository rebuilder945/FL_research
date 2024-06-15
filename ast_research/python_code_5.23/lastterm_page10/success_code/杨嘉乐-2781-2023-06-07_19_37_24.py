x=list(str(input()))
x1=list(map(int,x[:-1]))
xx="7－9－10－5－8－4－2－1－6－3－7－9－10－5－8－4－2".split("－")
xx=list(map(int,xx))
sum=0
for i in range(17):
    sum+=x1[i]*xx[i]
rest=sum%11
be=(12-rest)%11
if len(x)!=18:
    print("Error")
elif str(be)==x[17] or (be==10 and x[17]=="X"):
    print("Correct")
else:
    print("Wrong")
