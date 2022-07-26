# given N bulbs numbered 1-N that are arranged in a row
# the first bulb, index0, is plugged into a power socket
# each successive bulb is connected to the previous one
# the light switch is flipped at moment K (K goes 0 to N-1)
# at the 0th moment the switch for the corresponding index bulb is flipped on
# a light only shines when all previous light switches are on
# return the number of moments for which every turned on bulb shines

def solution(A):
    # dictionary comprehension with bulb # as key and false for 'on' property, flip to true when turned on
    bulb_status = {bulb_id: False for bulb_id in A}
    # init moment counter
    moment_couter = 0

    # loop through range of K moments, 0, len(A)
    for i in range(0, len(A)):
        # turn on A[i] in dictionary
        bulb_status[A[i]] = True
        # init boolean value to signify preceding bulbs are on
        on_boolean = False
        # loop through range of 1, (A[i] + 1)
        for j in range(1, (A[i] + 1)):
            # if dictionary[j] is true
            if bulb_status[j] is True:
                # on boolean = true
                on_boolean = True
            # else a preceding bulb is off and lights arent on
            else:
                # on boolean = false
                on_boolean = False
                # break the loop
                break

        # if on_boolean is true at end of loop
        if on_boolean is True:
            # incement the moment counter
            moment_couter += 1
    
    # return the moment counter
    return moment_couter

print(solution([2,1,3,5,4])) # 3
print(solution([2,3,4,1,5])) # 2
print(solution([1,3,4,2,5])) # 3
