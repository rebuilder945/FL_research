a=input()
b=input()
colorlist=['red','orange','yellow']
if a==b or a not in colorlist or b not in colorlist:
    print("error")
else:
    if a+b=="redblue" or a+b=="bluered":
        print("purple")
    elif a+b=="redyellow" or a+b=="yellowred":
        print("orange")
    elif a+b=="blueyellow" or a+b=="yellowblue":
        print("green")
