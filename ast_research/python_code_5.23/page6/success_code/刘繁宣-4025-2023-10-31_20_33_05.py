def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    n=num
    e=1
    for x in range(1,n+1):
        t=1
        for i in range(1,x+1):
            t=t*i
        e += 1/t
    print("%.6f"%e)
main()


