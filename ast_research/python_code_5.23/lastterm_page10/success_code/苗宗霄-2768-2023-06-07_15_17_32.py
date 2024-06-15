icard = input()
birthday = icard[6:14]  = f"{birthday[0:4]}-{birthday[4:6]}-{birthday[6:8]}"
mask = icard[:6] + "********" + icard[14:]
print(birthday)
print(mask)

