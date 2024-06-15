def main():
    num = eval(input())
    calculate_e(num)
 def calculate_e(num)：
            for i in range(num):
                lst=[]
                def factorial(i):
                    if i==0:
                        return 1
                    else:
                        return i* factorial(i-1)
                c=1/factorial(i)
                    lst.append(c)
            return "%.6f"%(sum(lst))
    return calculate_e(num)
main()


