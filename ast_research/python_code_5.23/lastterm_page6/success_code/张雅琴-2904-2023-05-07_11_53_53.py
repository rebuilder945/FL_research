def main():
    a=int(input())
    calculate_sum(a)
def calculate_sum(x):
    num=0
    for i in range(1,x+1):
        num1=0
        num1=num1*(10**len(str(x)))+x
    num+=num1
    print(num)

    

main()

