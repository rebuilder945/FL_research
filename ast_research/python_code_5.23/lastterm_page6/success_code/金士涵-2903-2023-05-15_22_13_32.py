def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=1
    e=1
    for i in range(1,num+1):
        n = n*i
        e = e+1/n
    print(round(e,6))

main()


