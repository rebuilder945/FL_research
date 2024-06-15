icard = input()
birthday = icard[6:14]
mask = "{}******{}"format(icard[0:7],icard[14:])
print(birthday)
print(mask)

