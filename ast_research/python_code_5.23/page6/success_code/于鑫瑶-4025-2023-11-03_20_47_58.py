def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=0
    e=1
    s=1
    for i in range(num):
        n=n+1
        s=n*s
        e+=1/s
    print(e)

main()


