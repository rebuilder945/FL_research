num = input()
if int(num) not in range(0,37):
    print('error')
else:
    if int(num)==0:
        print('green')
    elif int(num) in range(1,36,2):  # 奇数
        if int(num) in range(1,9) or int(num) in range(19,28):
            print('red')
        else:
            print('black')
    elif int(num) in range(2,37,2):
        if int(num) in range(1,11) or int(num) in range(19,29):
            print('black')
        else:
            print('red')
