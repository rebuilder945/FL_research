y1=input()
y2=input()
pc=['red','blue','yellow']
if y1 not in pc or y2 not in pc or y1==y2:
    print('error')
if y1=='red' and y2=='blue':
    print('purple')
if y1=='red' and y2=='yellow':
    print('orange')
if y1=='blue' and y2=='yellow':
    print('green')
if y2=='red' and y1=='blue':
    print('purple')
if y2=='red' and y1=='yellow':
    print('orange')
if y2=='blue' and y1=='yellow':
    print('green')
