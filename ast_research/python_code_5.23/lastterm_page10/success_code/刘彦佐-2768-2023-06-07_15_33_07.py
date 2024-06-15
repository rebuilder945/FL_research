icard = input()
birthday = "icard[6:10:1]"+"-"+"icard[10:12:1]"+"icard[12:14:1]"
mask = "icard[0:6:1]"+"*"*8+"icard[16:]"
print(birthday)
print(mask)

