def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    e=1
    c=1
    for i in range(1,num+1):
        c*=1/(1*i)
        e+=c
    print(e)
main()


