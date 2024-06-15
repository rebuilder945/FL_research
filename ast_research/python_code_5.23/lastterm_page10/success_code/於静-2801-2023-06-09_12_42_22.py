mima=input()
qiangdu=[0,0,0,0,0]
for x in mima:
    if "0"<=x<="9":
        qiangdu[0]=1
    if "a"<=x<="z":
        qiangdu[1]=1
    if "A"<=x<="Z":
        qiangdu[2]=1
    if len(mima)>=8:
        qiangdu[3]=1
    if x in"~!":
        qiangdu[4]=1
if len(mima)>=8:
    qiangdu[3]=1
print(qiangdu.count(1))

