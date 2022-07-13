# given array A consisting of N ints
# return the sum of all integers that ARE MULTIPLES OF 4

def solution(A):
    # init sum total counter for return value
    sum_total = 0
    # loop through A
    for num in A:
        # if num modulo 4 == 0 (remainder == 0)
        if num % 4 == 0:
            # add  num to sum total
            sum_total += num

    # loop finished, all multiples of 4 added to sum total, return the sum total
    return sum_total

print(solution([-6, -91, 1011, -100, 84, -22, 0, 1, 473]))
