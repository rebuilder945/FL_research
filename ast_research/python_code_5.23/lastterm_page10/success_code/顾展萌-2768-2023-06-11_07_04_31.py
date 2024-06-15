icard = input()
birthday = icard[6:14].replace("X", "0").replace("x", "0")
mask = icard[:6] + "********" + icard[-4:]
print(birthday)
print(mask)

