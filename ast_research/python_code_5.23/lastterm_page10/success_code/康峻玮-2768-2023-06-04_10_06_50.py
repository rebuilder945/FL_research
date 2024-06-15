icard = input()
birthday = icard[6:14]
mask = icard[:6] + "********"+ icard[-4:]
print(birthday)
print(mask)

