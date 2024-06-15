def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
        lst=[1]
        a=1
        for i in range(num):
                a=a*(i+1)
                b=1/a
                lst.append(b)
        c=sum(lst)
        print('%.6f'%c)
main()


