#电费计算：(期末读数 - 期初读数)*单价，电单价0.85元／度，电费保留两位小数
def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    cost = iConsume * 0.85

fElec1,fElec2=eval(input())
fee = costCompute(fElec1, fElec2).replace(“,”, " “))
print("%.2f"%fee)

