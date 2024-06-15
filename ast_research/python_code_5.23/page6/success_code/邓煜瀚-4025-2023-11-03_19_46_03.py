def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
        lst.append(1/factorial)
    print("%.6f"%sum(lst))
main()


