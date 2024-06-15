icard = input()
birthday = icard[7:14]
mask = icard.replace(icard[7:14],"********")
print(birthday)
print(mask)

