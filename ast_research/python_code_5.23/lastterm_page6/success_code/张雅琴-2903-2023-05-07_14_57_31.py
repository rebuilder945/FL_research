def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=1
    for i in range(1,num+1):
        b=1
        for x in range(1,i+1):
            b=b*x
        a=a+1/b
print("%.6f"%a)
main()


