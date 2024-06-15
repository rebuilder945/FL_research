def main():
    num = eval(input())
    calculate_e(num)
def  calculate_e(num):
        e = 2
         j = 1
        for i in range(1,num+1):
            j = j*i
           e +=1/j
       print(e)
main()


