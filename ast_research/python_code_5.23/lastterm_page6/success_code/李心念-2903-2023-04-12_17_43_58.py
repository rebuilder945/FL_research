def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    a = []
    for x in range(n):
        a.append((x+1)*(-1))
    print('%.6f'%(sum(a)))
main()


