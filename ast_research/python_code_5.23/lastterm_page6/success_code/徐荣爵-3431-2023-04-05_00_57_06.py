bag = ['green']
bag.extend(['red','black']*5)
bag.extend(['black','red']*4)
bag.extend(['red','black']*5)
bag.extend(['black','red']*4)
n = eval(input())
if n in list(range(37)):
    print(bag[n])
else:
    print('error')
