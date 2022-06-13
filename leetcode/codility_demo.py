# given a list A of N ints...
# return the smallest positive int (>0) that does not occur in A

def solution(A):
    # sort A
    # init min_positive as 1

    # loop through num in A
        # if num is > 0 and num == min_positive
            # min_postive += 1
    # return min_positive 

print(solution([1, 3, 6, 4, 1, 2])) # 5
print(solution([1, 2, 3])) # 4
print(solution([-1, -3])) # 1
