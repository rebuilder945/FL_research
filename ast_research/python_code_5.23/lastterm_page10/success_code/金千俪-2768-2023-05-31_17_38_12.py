icard = input()
birthday = "-".join(icard[6:10],icard[10:12],icard[12:14])
mask = icard.replace(icard[7:14],"********")
print(birthday)
print(mask)

