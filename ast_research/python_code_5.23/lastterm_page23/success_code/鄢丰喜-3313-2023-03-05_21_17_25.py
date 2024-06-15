consumption=eval(input())
fconsumption=input("点餐消费总额")
fcon=float(fconsumption)
ftip=fcon*0.1
ftax=fcon*0.07
ftoatl=fcon+ftax+ftip
sText="The consumption is %.4f,the tip is %.4f,the tax is %.4f,\
    so the total consumption is %.4f"%(fCon,fTip,fTax,fToatl)
print(sText)
sText=input()
print(sText.upper())
total=consumption+tip+tax
print("The consumption is %.4f, the tip is %.4f, the tax is %.4f,so the total consumption is %.4f"%(consumption,tip,tax,total))

