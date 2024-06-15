lstS = eval(input())
maxE = max(lstS)
minE = min(lstS)
lstR = [x for x in lstS if x!=maxE and x!=minE]
print(lstR)
