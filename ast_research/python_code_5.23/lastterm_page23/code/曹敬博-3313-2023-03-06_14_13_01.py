consumption=eval(input())
consumption=float(input("请输入消费金额”))
import consumption as c 
tip=c*0.1
tax=c*0.07
total=c+tip+tax
round(c,4)
round(tip,4)
round(tax,4)
a=total
round(a,4)
print("a")

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

