icard = input()
birthday = icard[6:10]+"-"+icard[11:13]+"-"+icard[13:15]
mask = icard[0:6]+"*"*8+icard[16::]
print(birthday)
print(mask)

