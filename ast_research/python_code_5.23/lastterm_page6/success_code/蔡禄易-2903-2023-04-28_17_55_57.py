def main():
    num = eval(input())
    calculate_e(num)
def calculate_e(num):
     e = 0
     for i in range (num):
            while num/1>1:
                num*=i
                e += 1/num
     print(e)
           
main()


