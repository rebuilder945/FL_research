def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    e=1
    b=1
    for i in range(0,a-1):
        b=b/(i+1)
        e+=b
    print(e)
main()


