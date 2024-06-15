consumption=eval(input())
consumption=100
print('%4f' % consumption)
tip=n*0.1
print('%4f' %tip)
tax=n*0.07
print('%4f' %tax)

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

