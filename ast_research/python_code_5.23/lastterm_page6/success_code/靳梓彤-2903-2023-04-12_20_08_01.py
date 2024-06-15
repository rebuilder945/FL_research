def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[1]
    a=1
    for i in range(num):
        a*=i
        b=1/a
        lst.append(b)
    print(sum(lst))
main()


