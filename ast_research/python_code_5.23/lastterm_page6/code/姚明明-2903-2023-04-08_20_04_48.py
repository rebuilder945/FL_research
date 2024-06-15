def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    for i in range(num):
        b=float(1/(i+1)!)
        lst.append(b)
    print("%.6f"%sum(lst))
main()


