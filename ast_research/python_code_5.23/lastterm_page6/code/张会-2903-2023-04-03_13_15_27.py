def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    a = 1
    for i in range(1,len(num)):
        b = 1 / i !
        a+=b
    print(a)
main()


