icard = input()
birthday = (f'{icard[7:11]}-{icard[11:13]}-{icard[13:15]}')
mask = (f'{icard[:7]}********{icard[17:]}')
print(birthday)
print(mask)

