# Write a program to calculate average temperature from user input

num_days = int(input('How many days do we have temperatures for? '))
total_of_temps = 0
temp_list = []

for i in range(num_days):
    next_day = int(input("Day" + str(i+1) + "'s high temp: "))
    temp_list.append(next_day)
    total_of_temps += temp_list[i]

avg = round(total_of_temps/num_days, 2)
print("Average Temperature = " + str(avg))

above_avg = 0
for i in temp_list:
    if i > avg:
        above_avg += 1
print(str(above_avg) + " day(s) above average")
