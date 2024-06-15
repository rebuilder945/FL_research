def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    c = []
    for x in range(num+1):
        a = 1
        for i in range(x):
             a = a*(i + 1)
        c.append(1/a)
    print("%.6f"%(sum(c)))
main()


