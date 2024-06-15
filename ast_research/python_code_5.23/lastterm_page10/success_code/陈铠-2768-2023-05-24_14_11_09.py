icard = input()
birthday = icard[6:14]
mask = icard.replace(icard[6:14],"********")
print(birthday)
print(mask)

