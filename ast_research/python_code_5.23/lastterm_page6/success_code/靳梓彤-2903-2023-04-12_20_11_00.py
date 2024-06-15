def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    a=1
    for i in range(1,num+1):
        a*=i
        b=1/a
        lst.append(b)
    print("%.6f"%sum(lst))
main()


