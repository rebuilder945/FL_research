icard = input()
birthday = icard[6:14]
mask = icard[:6]+"********"+icard[14:]
print(birthday)
print(mask)

