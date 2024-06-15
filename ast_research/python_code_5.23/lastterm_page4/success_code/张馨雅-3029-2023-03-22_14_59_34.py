names=input().split(",")
scores=eval(input())
names=list(names)
in1=()
out=[]
for i in range(len(names)):
    in1=(names[i],scores[i])
    out.append(list(in1))
print(out)
