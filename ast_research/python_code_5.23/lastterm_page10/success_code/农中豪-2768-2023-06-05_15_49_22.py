icard = input()
birthday = icard[7:11]+'-'+icard[11:13]+'-'+icard[11:15]
mask = icard[:7]+'*'*8+icard[-4:]
print(birthday)
print(mask)

