def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    e = 1
    for i in range(num):
        j = i+1
        t0 = 1
        for k in range(j):
            t0 = t0 * (k+1)
        t = 1 / t0
        e = e + t
    print('%.6f'%e)
main()


