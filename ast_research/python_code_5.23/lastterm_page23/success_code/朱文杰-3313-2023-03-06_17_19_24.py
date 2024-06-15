consumption=eval(input())
o=eval(input())
t=float(o*0.1)
c=float(o*0.07)
z=o+t+c

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

