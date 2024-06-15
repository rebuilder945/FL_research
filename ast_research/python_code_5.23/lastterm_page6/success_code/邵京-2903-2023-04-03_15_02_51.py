def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    e=1
    b=1
    for i in range(1,a+1):
        b=b*i
        e+=1/b
    print("%.4f"%e)
main()


