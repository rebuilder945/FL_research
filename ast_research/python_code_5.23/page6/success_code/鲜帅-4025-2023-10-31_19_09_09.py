def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    a=1
    b=1
    for i in range(1,x+1):
        for j in range(1,i+1):
            a*=j
        b+=1/a
    print("%.6f"%b)
main()


