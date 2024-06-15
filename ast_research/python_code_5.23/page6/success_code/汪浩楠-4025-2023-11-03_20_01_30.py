def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=0
    e=0
    b=1
    while a<=num:
        e+=b
        b=b*a
        a=a+1
    print(e)
main()


