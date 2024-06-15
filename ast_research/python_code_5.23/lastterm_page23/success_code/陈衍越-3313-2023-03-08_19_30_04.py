consumption=eval(input())
a=0.1
b=0.07
tip=float(consumption*a)
tax=float(consumption*b)

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

