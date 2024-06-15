consumption=eval(input())
tip=eval(0.1*consumption)
tax=eval(0.07*consumption)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

