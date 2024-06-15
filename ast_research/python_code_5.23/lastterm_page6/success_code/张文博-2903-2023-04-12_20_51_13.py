def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(a):
    e=1
    lst=[]
    i=1
    for x in range(a):
        b=1
        lst.append(x+1)
        i=i*lst[-1]
        e=e+1/i
    print("%.6f"%e)
main()


