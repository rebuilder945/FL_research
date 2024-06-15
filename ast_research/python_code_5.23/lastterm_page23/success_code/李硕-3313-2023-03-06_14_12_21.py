consumption=eval(input())
price = float(input())
tip = price*0.1
tax = price*0.07
total = price+tip+tax
print("the consumption is{:.4f},the tip is{:.4f},the tax is{:.4f},so the total consuption is {:.4f}".format(price, tip,tax,total))


total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

