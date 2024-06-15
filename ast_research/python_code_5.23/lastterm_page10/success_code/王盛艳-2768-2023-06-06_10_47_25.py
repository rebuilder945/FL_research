icard = input()
birthday = icard[6:10]+"-"+icard[11:12]+"-"+icard[13:14]
mask = icard[:6]+"********"+icard[14:]
print(birthday)
print(mask)

