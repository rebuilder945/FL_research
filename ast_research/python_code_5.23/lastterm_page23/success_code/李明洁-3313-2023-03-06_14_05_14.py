consumption=eval(input())
consumption=100
tip=consumption * 0.1
print("tip=",tip,type(tip))
tax=consumption * 0.07
print("tax=",tax)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

