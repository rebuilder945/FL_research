icard = input()
birthday = "{a}-{b}-{c}"\
 .format(a=icard[6:10],b=icard[10:12],c=icard[12:14])
mask = "{d}********{e}"\
 .format(d=icard[0:6],e=icard[14:])
print(birthday)
print(mask)

