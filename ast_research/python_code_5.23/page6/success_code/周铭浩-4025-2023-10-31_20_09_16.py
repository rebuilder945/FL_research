def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    y=1
    if num==1:
        print(e)
    else:
        for x in range(1,num+1):
            a=x
            for i in range(1,a):
                y=y*(y+1)
            e=e+1/y
    print(e)
main()


