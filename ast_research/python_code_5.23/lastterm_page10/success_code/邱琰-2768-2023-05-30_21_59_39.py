icard = input()
birthday = eval(str(icard[6,10])+"-"+str(icard[10,12])+"-"+str(icard[12,14]))
mask = eval(str(icard[0,6])+"********"+str(icard[14,18]))
print(birthday)
print(mask)

