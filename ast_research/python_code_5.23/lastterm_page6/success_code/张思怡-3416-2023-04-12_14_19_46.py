Money=input()
if Money.startswith('RMB'):
    Meiyuan=eval(Money[3:])/6.78
    print("USD%.2f"%(Meiyuan))
elif Money.startswith('&'):
    Meiyuan=eval(Money[1:])/6.78
    print("$%.2f"%(Meiyuan))
elif Money.startswith('USD'):
    Zhongyuan=eval(Money[3:])*6.78
    print("RMB%.2f"%(Zhongyuan))  
elif Money.startswith('$'):
    Zhongyuan=eval(Money[1:])*6.78
    print("&%.2f"%(Zhongyuan))
else:
   print("Error") 

