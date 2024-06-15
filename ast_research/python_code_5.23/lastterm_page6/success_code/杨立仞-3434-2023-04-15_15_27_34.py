a=input()
b=input()
if a+b=="red,blue" or b+a=="red,blue":
    print("purple")
elif a+b=="red,yellow" or b+a=="red,yellow":
    print("orange")
elif a+b=="blue,yellow" or b+a=="blue,yellow":
    print("green")
else:
    print("error")
