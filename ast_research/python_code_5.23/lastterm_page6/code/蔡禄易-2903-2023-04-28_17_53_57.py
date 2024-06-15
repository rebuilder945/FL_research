def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
     e = 0
     for i in range (num):
            num*=i
            e += 1/num
        a = e+1
        print(a)
           
main()


