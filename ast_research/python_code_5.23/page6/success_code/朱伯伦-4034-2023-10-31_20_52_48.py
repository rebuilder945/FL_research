from xml.etree.ElementPath import get_parent_map


a=input()
b=input()
ls=['red','blue','yellow']
if a==b or a not in ls or b not in ls:
    print('error')
else:
    if (a=='red' and b=='blue') or (a=='blue' and b=='red'):
        print('purple')
    elif (a=='red' and b=='yellow') or (a=='yellow' and b=='red'):
        print('orange')
    elif (a=='blue' and b=='yellow') or (a=='yellow' and b=='blue'):
        print('green')
    else:
        print('error')
