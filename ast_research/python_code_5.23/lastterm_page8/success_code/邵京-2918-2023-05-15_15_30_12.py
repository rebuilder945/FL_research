#电费计算：(期末读数 - 期初读数)*单价，电单价0.85元／度，电费保留两位小数
def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    return(0.85*(iConsume))

fElec1,fElec2=eval(input())
fee=costCompute(fElec1,fElec2)
print("%.2f"%fee)

