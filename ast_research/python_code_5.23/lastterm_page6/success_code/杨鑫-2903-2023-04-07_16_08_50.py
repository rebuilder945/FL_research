def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e = 1
    sum = 0
    for i in range(num):
        sum = sum + i
        e = e + 1/sum
    print("%.6f"%e)
main()


