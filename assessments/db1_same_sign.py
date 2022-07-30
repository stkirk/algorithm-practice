# Given an array on ints, numbers, and an int pivot
# return a new array in which the ith element equals
    # 0 if numbers[i] is 0
    # 1 if numbers[i] and pivot have the same sign
    # -1 if numbers[i] have different signs

def solution(numbers, pivot):
    # init return array
    return_array = []
    # init string rep for pivot
    sign = ""
    if pivot == 0:
        sign = "zero"
    elif pivot > 0:
        sign = "pos"
    else:
        sign = "neg"
    # loop nums in numbers
    for num in numbers:
        if num == 0:
            return_array.append(0)
        elif num > 0 and sign == "pos":
            return_array.append(1)
        elif num > 0 and sign == "neg":
            return_array.append(-1)

        elif num < 0 and sign == "pos":
            return_array.append(-1)
        elif num < 0 and sign == "neg":
            return_array.append(1)
    return return_array


print(solution([6, -5, 0], 2)) # [1, -1, 0]
