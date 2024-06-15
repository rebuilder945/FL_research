#电费计算：(期末读数 - 期初读数)*单价，电单价0.85元／度，电费保留两位小数
def costCompute(iStart, iEnd):
    iConsume = iEnd - iStart
    fElec1,fElec2=map(int,input().split(","))

fElec1,fElec2=eval(input())
cost=(fElec2-fElec1)*0.85
cost=(f2-f1)*0.8
print("%.2f"%fee)

