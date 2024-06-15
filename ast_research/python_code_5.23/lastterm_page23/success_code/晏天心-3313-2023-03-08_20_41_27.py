consumption=eval(input())

sMoney = input()
tTip = 0.1*sMoney
cTax = 0.07*sMoney
tAll = sMoney+tTip+cTax
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

