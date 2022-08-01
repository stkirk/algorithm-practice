# write a program that takes user int inputs and averages them together

user_nums = []
while True:
    inp = input('Add a number to the list: ')
    if inp == 'done':
        break
    value = float(inp)
    user_nums.append(value)

average = sum(user_nums) / len(user_nums)

print('Average', average)
