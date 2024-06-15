def colorname(a,b):
    colorset={'red','blue','yellow'}
    if a in colorset and b in colorset and a!=b:
        nameset={a,b}
        if 'red' in nameset and 'blue' in nameset:
            print('purple')
        elif 'yellow' in nameset and 'blue' in nameset:
            print('green')
        elif 'red' in nameset and 'yellow' in nameset:
            print('orange')
    else:
        print('error')
name1=input()
name2=input()
colorname(name1,name2)

