consumption=eval(input())
a=eval(input())
b=("%.4f"%(a/10))
c=("%.4f"%(a))
d=("%.4f"%(a*0.7))
e=("%.4f"%(1.17*a))
print('The consumption is',c,'the tip is',b,'the tax is',d,'so the total consumption is',e)

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

