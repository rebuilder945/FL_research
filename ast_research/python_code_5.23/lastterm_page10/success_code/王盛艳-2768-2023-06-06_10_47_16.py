icard = input()
birthday = icard[6:10]+"-"+icard[11:12]+"-"+icard[13:14]
mask = icard[:7]+"********"+icard[14:]
print(birthday)
print(mask)

