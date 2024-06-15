def main():
    num = eval(input())
    calculate_e(num)
    print("%.6f"%calculate_e(num))
def calculate_e(num):
    a=1
    b=1
    for i in range(1,num+1):
        b=b*i
        c=1/b
        a += c
    return(a)

main()


