consumption=eval(input())
def iftax(consumption):
    iftax = consumption*0.07
    return itax
tax = iftax(consumption)

def iftip(consumption):
    itip = consumption*0.1
    return itip
tip = iftip(consumption)

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

