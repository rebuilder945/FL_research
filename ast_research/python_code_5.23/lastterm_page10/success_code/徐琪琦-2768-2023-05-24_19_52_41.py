icard = input()
birthday = icard[8:12:]+"-"+icard[12:14:]+"-"+icard[14:16:]
mask = icard.replace(icard[8:16:],"********")
print(birthday)
print(mask)

