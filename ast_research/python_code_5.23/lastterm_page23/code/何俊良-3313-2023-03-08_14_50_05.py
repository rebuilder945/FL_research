consumption=eval(input())
meal cost=float(input(‘请输入总餐费:’))
tip=meal cost*0.1
tax=meal cost*0.07
total cost=meal cost+tip+tax
print(f"餐费:{meal cost:.4f}")

total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

