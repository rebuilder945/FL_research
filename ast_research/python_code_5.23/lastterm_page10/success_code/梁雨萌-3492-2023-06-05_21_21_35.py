word = input() or 'None'

if word == 'None':
    print(word)
else:
    for i in word:
        if word.count(i) == 1:
            a = i
            break
print(a) 
