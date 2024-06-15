def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    e=1
    for i in range(x):
        m=1/[(i+1)!]
        e+=m
    print(e)
main()


