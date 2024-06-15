consumption=eval(input())
a=float(consumption)*0.1
tip="%.4f"%(a)
tip=float(tip)
b=float(consumption)*0.07
tax="%.4f"%(b)
tax=float(tax)
consumption=float(consumption)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

