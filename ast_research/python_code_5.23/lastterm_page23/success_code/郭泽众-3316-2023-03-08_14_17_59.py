nMal=int(input())
nFem=int(input())
nAll=nMal+nFem
perM="%.2f"%float(nMal/nAll*100)
perF="%.2f"%float(nFem/nAll*100)
print("The male students ratio is", perM, "%,the female students ratio is", perF, "%")
