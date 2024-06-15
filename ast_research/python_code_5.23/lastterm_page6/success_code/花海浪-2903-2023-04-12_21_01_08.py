def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    b=[]
    for i in range(1,num+1):
        a=a*i
        b.append(1/a)
    e=1+sum(b)
    print("%.6f"%(e))
main()


