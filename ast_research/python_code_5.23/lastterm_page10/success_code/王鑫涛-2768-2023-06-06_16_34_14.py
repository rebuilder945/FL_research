icard = input()
birthday = icard[6:10]+"-"+icard[10:12]+"-"+icard[13:15]
mask = icard.replace(icard[6:15],"********")
print(birthday)
print(mask)

