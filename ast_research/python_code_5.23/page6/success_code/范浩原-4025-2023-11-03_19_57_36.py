def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    for i in range(1,num+1):
        b*=i
        a+=1/b
    print("%.6f"%a)
main()


