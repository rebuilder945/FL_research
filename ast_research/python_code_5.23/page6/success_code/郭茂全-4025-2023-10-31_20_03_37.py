def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=0
    y=1
    for x in range(num):
        y*=(x+1)
    for x in range(num):
        b=(x+1)/y
        e+=b
    print(e)
main()


