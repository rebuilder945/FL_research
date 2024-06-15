icard = input()
birthday = icard[6:10]
mask = icard[:6]+"******"+icard[14:18]
print(birthday)
print(mask)

