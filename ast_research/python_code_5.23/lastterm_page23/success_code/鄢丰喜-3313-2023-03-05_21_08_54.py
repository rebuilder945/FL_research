consumption=eval(input())
fconsumption=input("点餐消费总额")
fCon=float(fConsumption)
fTip=fCon*0.1
fTax=fCon*0.07
fToatl=fCon+fTax+fTip
sText="The consumption is %.4f,the tip is %.4f,the tax is %.4f,\
    so the total consumption is %.4f"%(fCon,fTip,fTax,fToatl)
print(sText)
sText=input()
print(sText.upper())
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

