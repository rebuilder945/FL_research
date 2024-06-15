icard = input()
birthday = icard[6:13]
mask = icard[0:6]+"*"*6+icard[13:]
print(birthday)
print(mask)

