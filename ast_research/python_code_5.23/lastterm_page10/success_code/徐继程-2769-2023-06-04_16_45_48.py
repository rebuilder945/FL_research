numb=input()
print(numb)
for i in numb:
    nums=set(numb)
for x in nums:
    if ord(x)>=ord('a') and ord(x)<=ord('z'):
        numb=numb.replace(x,chr(25-ord(x)+2*ord('a')))
    elif ord(x)>=ord('A') and ord(x)<=ord('Z'):
        numb=numb.replace(x,chr(25-ord(x)+2*ord('A')))
print(numb)    


