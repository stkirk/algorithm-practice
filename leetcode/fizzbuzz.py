# Given a number, n, for each integer i in the range 1 to n(inclusive):
# if i is...
# a multiple of both 3 and 5 print "FizzBuzz"
# a multiple of 3 but not 5 print "Fizz"
# a multiple of 5 but not 3 print "Buzz"
# not a multiple of either print i

def fizz_buzz(n):
    # loop through range 1, n+1
        # if i mod 3 == 0 and i mod 5 == 0
            # print("FizzBuzz")
        # elif i mod 3 == 0 and i mod 5 != 0
            # print("Fizz")
        # elif i mod 3 != 0 and i mod 5 == 0
            # print("Buzz")
        #else:
            # print(i)
    print(n)

fizz_buzz(15)
# prints 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
