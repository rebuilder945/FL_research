def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    y=1
    for x in range(num):
        y*=(x+1)
        b=1/y
        e+=b
    print(e)
main()


