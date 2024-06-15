def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    b=0
    a=1
    for x in range(0,num+1,1):
        a=a*x
        b=b+1/(a**1)
    print(b)
main()


