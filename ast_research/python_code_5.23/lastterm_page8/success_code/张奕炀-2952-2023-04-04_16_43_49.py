def print_matrix(n):
    list0 = list(range(number))
    list0.append(number)
    list0.pop(0)
    list0 = list(map(str,list0))
    for i in range(number):
        list1 = list0[0:i+1] + [str(i+1)]*(number-i-1)
        answer = ""
        for i in range(len(list1)):
            answer = answer + list1[i]
        answer = list(answer)
        answer0 = " ".join(answer)
        print(answer0)

number=eval(input())
print_matrix(number)



