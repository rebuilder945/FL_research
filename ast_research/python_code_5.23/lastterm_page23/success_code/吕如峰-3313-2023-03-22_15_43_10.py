consumption=eval(input())
consumption=float(("%.4f"%(consumption)))
tip=float(("%.4f"%(consumption/10)))
tax=float(("%.4f"%(consumption*0.07)))

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

