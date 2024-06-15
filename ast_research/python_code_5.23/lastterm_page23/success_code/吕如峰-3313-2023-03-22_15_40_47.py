consumption=eval(input())
a=eval(input())
b=float(("%.4f"%(a/10)))
c=float(("%.4f"%(a)))
d=float(("%.4f"%(a*0.7)))
e=float(("%.4f"%(1.17*a)))

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

