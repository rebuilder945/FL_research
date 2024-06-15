a=input()
a.strip('[')#从前往后找第一个并删除
a.rstrip(']')#从后往前
L=a.split(",")
b=[]
for i in L:
     b.append(int(i))
h=[]
for i in b:
    n=b.count(i)
    if n==1:
        h.append(int(i))
    else:
        None
h.sort()
if h==[]:
    print(False)
else:
    print(",".join(map(str,h)))





