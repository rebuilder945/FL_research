def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 0
    a = 1
    for x in range(num):
        a = a * (1/x)
        e +=a
    print(a)
main()


