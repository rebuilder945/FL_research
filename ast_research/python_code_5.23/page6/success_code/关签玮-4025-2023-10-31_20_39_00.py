def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[1]
    for i in range(1,num+1):
        a=1
        for x in range(1,i+1):
            a=a*x
        b=1/a
        lst.append(b)
    print("%.6f"%(sum(lst)))
main()


