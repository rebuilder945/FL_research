def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
    b=1
    a=1
    for x in range(1,num+1,1):
        a=a*x
        b=b+1/(a)
    print(b)
main()


