m=input().split(" ")
print(m)
a=0
for x in m:
    a += len(x)
print(str(len(m))+","+"%.2f" %(a/len(m)))

