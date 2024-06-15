icard = input()
birthday = icard[6:10]+"-"+icard[10:12]+"-"+icard[14:46]
mask = icard[:6]+"*"*8+icard[14:]
print(birthday)
print(mask)

