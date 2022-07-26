''' 
Write a function that takes two inputs, n and m, representing height and width of a grid that
outputs the number of unique paths from the top left corner of the grid to the bottom right
corner
***Constraint*** Can only move down or right one unit at a time
'''
# Step 1 - Simpleist possible input?
    # 1x1 grid with only 1 path
    # a grid with either m or n == 1 only has 1 path
    # Base Case: if n = 1 or m = 1 return 1
# Step 2 - Visualize Examples
# Step 3 - Relate hard cases to simpler cases
    # take a 3x2 and 2x3 grid and compare to a 3x3
        # each path from 3x2 and 2x3 need 1 extra move to create all the paths when overlayed on the 3x3 grid
        # number of solutions for 3x3 = unique_grid_paths(2,3) + unique_grid_paths(3,2)
    # double check if this is true or coincidence with 3x4 and 3x3/2,4
# Step 4 - Generalize the Pattern
    # unique_grid_paths(n,m) = unique_grid_paths(n, m-1) + unique_grid_paths(n-1, m)
# Step 5 - Combine Base case and Generalized Recursive Case
def unique_grid_paths(n,m):
    # Base Case:
    if n == 1 or m == 1:
        return 1
    # Recursive Case:
    else:
        return unique_grid_paths(n, m-1) + unique_grid_paths(n-1, m)

print(unique_grid_paths(3,3))
