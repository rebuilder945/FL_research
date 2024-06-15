def  costCompute(iStart,  iEnd):
        iConsume  =  iEnd  -  iStart
        fee=iConsume*0.85


fElec1,fElec2=eval(input())
costCompute(fElec1,fElec2)
print("%.2f"%fee)

