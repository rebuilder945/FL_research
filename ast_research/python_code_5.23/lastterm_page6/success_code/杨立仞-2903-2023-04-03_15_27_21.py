def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e=1
    s=1
    for x in range(1,n+1):
        s*=x
        e+=1/s
    print("{:.6f}".format(e))
main()


