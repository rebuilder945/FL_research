def main():
    num = eval(input())
    calculate_e(num)
    
    def calculate_e(num):
        def j(num):
            if num == 0:
                return 1
            else:
                return n * j(num-1)
        a=1
        for i in range(1,num+1):
            a+=1/j(i)
       return a     
print(calculate_e(num))
                
main()


