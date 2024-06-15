def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
    for i in range(1,num+1,1):
        x=1/(i!)
        e=1
        e=e+x
     print(e)
main()


