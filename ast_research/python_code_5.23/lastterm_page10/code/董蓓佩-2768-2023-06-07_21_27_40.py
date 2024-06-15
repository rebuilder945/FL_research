icard = input()
birthday = icard[7:15]
mask = icard[1:7]+**8+icard[17:]
print(birthday)
print(mask)

