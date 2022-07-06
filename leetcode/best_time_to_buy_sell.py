# Given an array of ints, prices, where prices[i] is the price of a given stock on the ith day:
# Return the maximum profit you can achieve by choosing a day to buy and sell
# If no profit can be achieved return 0

def max_profit(prices):
    # init max_profit to 0

    # memoize the buy index and init buy index to first price in prices

    # loop through i, price in prices
        # init cur_profit to price - prices[buy_idx]

        # if the cur_profit > max_profit:
            # set new max profit
            # max_profit = cur_profit

        # if the price is less than buy index price
            # set buy index to current index

    # return the max profit
    return prices

print(max_profit([7,1,5,3,6,4])) # 5 --> buy on day 2 sell on day 5
print(max_profit([7,6,4,3,1])) # 0
