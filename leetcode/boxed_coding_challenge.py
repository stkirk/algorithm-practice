# Given a string, S, consisting of N lines that are separated by ASCII code 10
# Each line describes a phone call using the format "hh:mm:ss,nnn-nnn-nnn"
# the first part denotes duration of call hours:minutes:seconds
# second part denotes the 9 digit phone number of the recipient with no leading zeroes

# Each call is billed seperately
# Billing rules:
# if a call was < 5 minutes --> you pay 3 cents for every second of the call e.g. 67 second call you pay 67*3==201 cents
# if the call was >= 5 minutes --> you pay 150 cents for every started minute of the call
# e.g a 5 minute call you pay 5*150 but a 5 minute and one second call you pay 6*150
# All calls to the phone number that has the longest total duration of calls is free
# if there is more than 1 number that share the longest duration the promotion is applied to the number whose numerical value is smallest among the phone numbers

# Return the amount of money you have to pay in cents

# line break character --> ord(index in the string) == 10 thats where we do our split

import math


def solution(S):
    # break S down into list where each item is a list with 0 index being call length and 1st index being phone number
    split_list = S.split(chr(10))
    # list comprehension to get them into indexes of lists
    call_list = [call.split(",") for call in split_list]

    # init bill_total to 0
    bill_total = 0
    # keep a total charge for all phone numbers in a hash table
    phone_num_to_charge = {}
    # save phone number of total longest call duration
    phone_number_for_promo = ""

    #loop each call in the call_list and calculate the cost of the call
    for call in call_list:
        # calculate duration of call in seconds
        call_duration = int(call[0][0:2]) * 3600 + int(call[0][3:5]) * 60 + int(call[0][6:])

        if call_duration < 300:
            # call_cost = duration * 3 cents
            call_cost = call_duration * 3

            # if phone number is in the hash map
            if call[1] in phone_num_to_charge:
                # increment its total call cost and duration
                phone_num_to_charge[call[1]]["duration"] += call_duration
                phone_num_to_charge[call[1]]["cost"] += call_cost
            # else the phone number isnt in there
            else:
                # add phone number and cost
                phone_num_to_charge[call[1]] = {"duration": call_duration, "cost": call_cost}

            # increment bill total by call_cost
            bill_total += call_cost

        # else call_duration >= 300:
        else:
            # call_cost = call_duration / 60 and round up to next minute * 150 cents
            call_cost = math.ceil(call_duration / 60) * 150

            # if phone number is in the hash map
            if call[1] in phone_num_to_charge:
                # increment its total call cost and duration
                phone_num_to_charge[call[1]]["duration"] += call_duration
                phone_num_to_charge[call[1]]["cost"] += call_cost
            # else the phone number isnt in there
            else:
                # add phone number and cost
                phone_num_to_charge[call[1]] = {"duration": call_duration, "cost": call_cost}
            # increment bill total by call_cost
            bill_total += call_cost

        # if total duration from this call's number is greater than or equal to existing:
        if not phone_number_for_promo:
            phone_number_for_promo = call[1]
        elif phone_num_to_charge[call[1]]["duration"] == phone_num_to_charge[phone_number_for_promo]["duration"]:
            # convert both phone numbers to ints
            current_phone = ""
            existing_phone = ""
            for i in range(len(call[1])):
                if call[1][i] != "-":
                    current_phone += call[1][i]
                    existing_phone += phone_number_for_promo[i]
            if int(current_phone) < int(existing_phone):
                phone_number_for_promo = call[1]
        elif phone_num_to_charge[call[1]]["duration"] > phone_num_to_charge[phone_number_for_promo]["duration"]:
            phone_number_for_promo = call[1]

    # return bill_total - the cost associated with the phone_number_for_promo in the dictionary
    return bill_total - phone_num_to_charge[phone_number_for_promo]["cost"]

print("return value", solution("""00:01:00,400-234-090
00:01:00,400-234-090
00:01:00,400-234-090
00:06:00,701-080-080
00:01:00,400-234-090
00:01:00,400-234-090
00:01:00,400-234-090""")) #900
print("return value", solution("""00:05:00,701-080-080
00:05:00,400-234-090""")) #750
print("return value", solution("01:01:07,701-080-080")) #0
print("return value", solution("""01:01:07,701-080-080
01:01:07,701-080-080
01:01:07,601-080-080""")) #9300
