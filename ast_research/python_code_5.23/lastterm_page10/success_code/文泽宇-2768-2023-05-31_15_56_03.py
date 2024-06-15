icard = input()
birthday =  '{a}-{b}-{c}'.format(a=icard[6:10],b=icard[10:12],c=icard[12:14])
mask = '{}{ok}{d}'.format(icard[0:6],ok='********',d=icard[-4:]) 
print(birthday)
print(mask)

