#电费计算：(期末读数 - 期初读数)*单价，电单价0.85元／度，电费保留两位小数
def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    fUnitPrice = 0.85 
    fFee = iConsume * fUnitPrice  # 电费
    return fFee

fElec1,fElec2=eval(input())
costCompute(iStart, iEnd)
print("%.2f"%fee)

