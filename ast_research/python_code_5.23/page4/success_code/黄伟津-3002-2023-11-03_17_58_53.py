sFigure = eval(input())
xlist = [int(sFigure[i]) for i in range(len(sFigure))]
fAverage = sum(xlist) / len(xlist)
print("%.2f"%fAverage)
