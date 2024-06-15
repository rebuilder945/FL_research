consumption=eval(input())
tip = float(consumption*10%)

tax = float(consumption*7%)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

