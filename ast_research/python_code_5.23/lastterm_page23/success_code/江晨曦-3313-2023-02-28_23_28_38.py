consumption=eval(input())
def calculate(c):
    c1 = c*0.1
    c2 = c*0.07
    return c1,c2
tip,tax=calculate(consumption)
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

