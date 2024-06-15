nMal=int(input())
nFem=int(input())
nAll=nMal+nFem
perM=float(nMal/nAll*100)
perF=float(nFem/nAll*100)
print(f"The male students ratio is {perM:.2f}%,the female students ratio is {perF:.2f}%")
