icard = input()
birthday = "-".join(list(icard)[6:10],list(icard)[10:12],list(icard)[12,14])
mask = icard.replace(icard[6:14],"********")
print(birthday)
print(mask)

