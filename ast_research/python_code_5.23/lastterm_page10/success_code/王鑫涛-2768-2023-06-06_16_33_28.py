icard = input()
birthday = icard[6:10]+"-"+icard[10:12]+"-"+icard[14:16]
mask = icard.replace(icard[6:16],"********")
print(birthday)
print(mask)

