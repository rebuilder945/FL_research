icard = input()
birthday = icard[6:10]+"-"+icard[10:12]+"-"+icard[12:15]
mask = icard[0:6]+"********"+icard[15:-1]
print(birthday)
print(mask)

