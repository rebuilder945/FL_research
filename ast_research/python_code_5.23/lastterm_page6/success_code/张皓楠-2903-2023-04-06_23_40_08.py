def main():
    num = eval(input())
    calculate_e(num)
def jie(a):
    b = 1
    for i in range(a):
        b*=i+1
    return b
def calculate_e(a):
    b = 1
    for i in range(a):
        b += 1/jie(i+1)
    print(b)
main()


