icard = input()
birthday = icard[6:10]+"-"+icard[10:12]+"-"+icard[12:14]
mask = icard[1:6]+"********"+icard[14:18]
print(birthday)
print(mask)

