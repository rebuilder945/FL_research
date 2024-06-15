jack=[]
while True:
    a=input()
    if a!='#':
        jack.append(eval(a))
    else:
        print(len(jack),sum(jack))
        break
