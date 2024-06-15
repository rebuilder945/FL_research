icard = input()
birthday = icard[6:9]+"-"+icard[10:11]+"-"+icard[12:13]
mask = icard.replace(icard[6:13],"********")
print(birthday)
print(mask)

