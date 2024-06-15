icard = input()
birthday = icard[6:9]+"-"+icard[10:11]+"-"+icard[14:15]
mask = icard.replace(icard[6:15],"********")
print(birthday)
print(mask)

