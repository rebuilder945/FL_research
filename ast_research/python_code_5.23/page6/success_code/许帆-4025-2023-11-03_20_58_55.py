def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    x=1
    for i in range(1,num+1):
        x = x*(1/i)
        e += x
    print(e)

main()


