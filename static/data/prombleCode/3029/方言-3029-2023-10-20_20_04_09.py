xm=input().split(",")
fs=input()
n=len(xm)
fsl=""
fsll=[]
for i in range(len(fs)):
    if fs[i] in '0123456789':
        fsl+=fs[i]
    if fs[i]=="," or fs[i]=="]":
        fsll.append(int(fsl))
zt=[]
for i in range(3):
    print(i)
    ab=[] 
    ab.append(xm[i])
    ab.append(fsll[i])
    zt.append(ab)
print(zt)
