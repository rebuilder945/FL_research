def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    m=1
    for i in range(num):
        y=1
        for x in range(i+1):
            y*=x+1
        m+=1/y
    print(m)
main()


