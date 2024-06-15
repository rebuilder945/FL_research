def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(x):
    last=1
    for i in range(1,x+1):
        eva=1
        for j in range(1,i+1):
            eva*=j
        last+=1/eva
    print('%.6f'%last)
main()


