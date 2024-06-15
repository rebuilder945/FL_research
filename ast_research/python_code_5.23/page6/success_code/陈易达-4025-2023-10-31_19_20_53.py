def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(n):
    e = 2
    for x in range(1,n+1):
        y = 1
        for i in range(1,x+1):
            y += y*i
        e += 1/y
    print("%.6f"%e)
main()


