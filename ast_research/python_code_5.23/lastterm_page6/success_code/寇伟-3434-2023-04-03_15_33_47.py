def judge_color(co1,co2):
    if co1=='red' and co2=='blue':
        print('purple')
    elif co2=='red' and co1=='blue':
        print('purple')
    elif co1=='red' and co2=='yellow':
        print('orange')
    elif co2 == 'red' and co1 == 'yellow':
        print('orange')
    elif co1=='blue' and co2=='yellow':
        print('green')
    elif co1 == 'blue' and co2 == 'yellow':
        print('green')
    else:
        print('error')
co1=input()
co2=input()
judge_color(co1,co2)
