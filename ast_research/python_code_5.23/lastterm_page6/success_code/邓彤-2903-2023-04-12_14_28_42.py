def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=(1+1/num)**num
    print("%.6f"(e))
main()


