def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    a=[1]
    for i in range(1,x+1):
        b=1
        for n in range(1,i+1):
            b=b*1/n
            a.append(b)
    print(sum(a))
main()


