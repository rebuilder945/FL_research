icard = input()
birthday = f"{idcard[6:10]}-{idcard[10:12]}-{idcard[12:14]}"
mask = idcard[:6]+'*'*8+idcard[14:]
print(birthday)
print(mask)

