def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
        e=0
        b=1
        for x in range(1,a+1):
                b*=x
                c=1/b
                e+=c
        print(e)
main()


