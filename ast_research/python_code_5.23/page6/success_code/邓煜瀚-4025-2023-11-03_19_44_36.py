def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
        lst.append(factorial)
    print(sum(lst))
main()


