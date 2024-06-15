icard = input()
birthday = "-".join(icard[6:14:2])
mask = icard.replace(icard[7:14],"********")
print(birthday)
print(mask)

