def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[1]
    for i in range(1,num+1):
        num=1*i
        a=1/num
        lst.append(a)
    print("%.6f"%sum(lst))
main()


