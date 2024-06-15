icard = input()
birthday = icard[6:11]+"-"+icard[11:13]+"-"+icard[13:15]
mask = icard[:6]+"********"+icard[15:]
print(birthday)
print(mask)

