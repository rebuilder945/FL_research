def test_string_unique(arr):
    dic = {}
    if not arr:
        return 'None'
    for index in range(len(arr)):
        if arr[index] in dic:
            dic[arr[index]] += 1
        else:
            dic[arr[index]] = 1
    
    for j in dic:
        if dic[j] == 1:
            result = arr.index(j)
            break
    return result


