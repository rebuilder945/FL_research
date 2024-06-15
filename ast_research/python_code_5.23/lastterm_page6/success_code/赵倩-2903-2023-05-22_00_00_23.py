def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    t=1
    for x in range(1,n):
        t*=x
        s+=(1/t)
        print(":.6f".format(s))
main()


