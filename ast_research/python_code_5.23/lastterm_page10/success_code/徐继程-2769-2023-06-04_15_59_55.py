numb=input()
print(numb)
for x in range(len(numb)):
    ordx=ord(numb[x])
    if ordx>=ord('a') and ordx<=ord('z'):
        numb=numb.replace(numb[x],chr(26-ord(numb[x])+ord('a')))
    elif ordx>=ord('A') and ordx<=ord('Z'):
        numb=numb.replace(numb[x],chr(26-ord(numb[x])+ord('A')))
print(numb)    


