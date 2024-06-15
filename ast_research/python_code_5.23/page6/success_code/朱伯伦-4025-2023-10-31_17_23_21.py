def main():
    num = eval(input())
    calculate_e(num)
def calculate_e():
    e=0
    for i in range(num):
        a=1/(i+1)
        e+=a
    print (e)

main()


