consumption=eval(input())
c=float(("%.4f"%(consumption)))
b=float(("%.4f"%(consumption/10)))
d=float(("%.4f"%(consumption*0.7)))
e=float(("%.4f"%(1.17*consumption)))

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

