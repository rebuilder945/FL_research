def main():
    num = eval(input())
    calculate_e(num)
 def caculate_e(num):
        e = 1
        n = 1
        for x in range(1,num+1):
            n *= x
            e += 1/n 
        print("%.6f"%e)

main()


