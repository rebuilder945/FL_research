def print_matrix(n):
        for i in range(1,n+1):
            num = 1
            for each in range(1,n+1):
                if num < i:
                    print(num,end = ' ')
                    num += 1
                else:
                    print(num,end = ' ')
            print()
    else:
        print('请输入1到9之间的整数！')


number=eval(input())
print_matrix(number)



