icard = input()
birthday = icard[7:11]-icard[11:13]-icard[13:15]
mask = icard[0:7]+"*"*8+icard[15:19]
print(birthday)
print(mask)

