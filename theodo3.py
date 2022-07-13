# Given an array of blocks with N integers denoting their heights
# return the longest possible distance 2 frogs can make between each other if they can only move to an adjacents block that is >= the one they are on in height
# assume they ALWAYS choose the optimal starting block

def solution(blocks):
    # init a max distance counter to 0
    max_distance = 0

    # loop through blocks and compute the max distance the frogs can move from each other if that was their starting block
        # init current max distance for each loop to 1 (K-J + 1), increment as moves are made
        # move frog1 to the right as far as they can go
        # 

