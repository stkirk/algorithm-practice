# Given a staircase with n steps, and a restriction that you can only climb 1 or 2 steps at a time
# In how many distinct ways can you climb to the top?

# have a choice at each step, climb 1 step or 2
# this pattern repeats over and over

def climb_stairs(n):
    # base case: last two steps each with 1 way to get to nth step
    first, second = 1, 1
    # loop n-1 times to work back to 0th step
    for i in range( n - 1):
        # at each step, store old first
        old_first = first
        # update new first to first plus second
        first = first + second
        # set second to old first
        second = old_first

    # return first (now at 0th step)    
    return first

print(climb_stairs(2)) # 2
print(climb_stairs(3)) # 3
