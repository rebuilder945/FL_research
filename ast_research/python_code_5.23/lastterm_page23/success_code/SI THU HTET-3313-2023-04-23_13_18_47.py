consumption=eval(input())
cost = float(input())

tip = cost * 0.1
tax = cost * 0.07
total_cost = cost + tip + tax

print("The consumption is {:.4f}, the tip is {:.4f}, the tax is {:.4f},so the total consumption is {:.4f}".format(cost, tip, tax, total_cost))


total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

