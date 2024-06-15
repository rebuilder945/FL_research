def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    b=1
    a=1
    for x in range(num):
        while x>0:
            x-=1
            e+=1/a
            b+=1
            a=a*b
    print("%.6f"%e)
main()


