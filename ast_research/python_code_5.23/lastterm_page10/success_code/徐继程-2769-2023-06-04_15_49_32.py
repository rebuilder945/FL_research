numb=input()
print(numb)
for x in range(len(numb)):
    ordx=ord(numb[x])
    if ordx>=ord('a') and ordx<=ord('z'):
        numb.replace(numb[x],chr(27-ord(numb[x])))
    elif ordx>=ord('A') and ordx<=ord('Z'):
        numb.replace(numb[x],chr(27-ord(numb[x])))
print(numb)    
