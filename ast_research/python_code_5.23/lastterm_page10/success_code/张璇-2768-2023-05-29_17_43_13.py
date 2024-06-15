icard = input()
birthday = "-".join(str(icard[6:10]),str(icard[10:12]),str(icard[12:14]))
mask = icard.replace(icard[6:14],"********")
print(birthday)
print(mask)

