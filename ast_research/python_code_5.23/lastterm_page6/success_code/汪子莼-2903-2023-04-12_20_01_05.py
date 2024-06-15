def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    lst=[]
    a=1
    lst.append(a)
    for i in range(num):
        b=1/i
        lst.append(b)
    print(sum(lst))
        
main()


