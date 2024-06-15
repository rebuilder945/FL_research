word = input() or 'None'

if word !='None':
    for i in word:
        if word.count(i) == 1:
            word = i
            break
print (word)
    
