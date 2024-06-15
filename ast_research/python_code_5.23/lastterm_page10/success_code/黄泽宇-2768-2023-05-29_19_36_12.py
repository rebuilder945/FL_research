icard = input()
birthday = icard[6:10]+"-"+icard[11:12]+"-"+icard[13:14]
mask = icard[0:6]+"*"*8+icard[15::]
print(birthday)
print(mask)

