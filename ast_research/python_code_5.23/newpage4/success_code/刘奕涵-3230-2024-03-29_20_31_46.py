def largest_number(nums):
    nums=list(dict.fromkeys(nums))
    def sort_keys(num_str):
        return int(''.join(sorted([num_str]+[str(num) for num in nums if num !=int(num_str)],reserve=True)))
    sorted_nums=sorted(map(str,nums),key=sort_keys,reserve=True)
    result=''.join(sorted_nums)
