consumption=eval(input())
consumption=100
tip=100 * 0.1
print("tip=",tip,type(tip))
tax=100* 0.07
print("tax=",tax)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

