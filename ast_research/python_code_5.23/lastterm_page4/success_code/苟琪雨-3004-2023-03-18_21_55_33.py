def get_prime(a_list):
    
    final_list = []

    for num in a_list:


        if (num == 0) or (num == 1):

            continue

        elif num == 2:

            final_list.append(2)

        else:
            flag = 0
            for i in range(2,num-1):
                if num%i == 0:
                    flag +=1

            if flag == 0:
                final_list.append(num)
                
    return final_list
    
a_list = eval(input())

print(get_prime(a_list))

