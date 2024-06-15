icard = input()
birthday = '-'.join((icard[5:9],icard[9:11],icard[11:13]))
mask = icard.replace((icard[6:13],'********'))
print(birthday)
print(mask)

