def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    s=1
    for x in range(1,num+1):
        b=1
        for i in range(1,x+1):
            b=b*i
        s=s+1/b
    print(s)

main()


