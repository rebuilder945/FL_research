icard = input()
birthday =  icard[6:9]+'-'+icard[10:11]+'-'icard[12:13]
mask = icard[0:5]+'*'*8+icard[14:]
print(birthday)
print(mask)

