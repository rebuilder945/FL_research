def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    a=[1]
    for i in range(1,num+1):
        b=1
        for x in range(1,i+1):
        b*=x
    a.append(b)
    c=sum(a)
    print("%.6f"%c)

main()


