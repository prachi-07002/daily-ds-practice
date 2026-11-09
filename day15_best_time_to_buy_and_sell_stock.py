"""
Day 15 - 2026-10-25
NeetCode 150: Sliding Window
Problem: Best Time to Buy and Sell Stock (LeetCode 121)

Problem statement:
You are given an array `prices` where `prices[i]` is the price of
a given stock on the `i`th day.

You want to maximize your profit by choosing a single day to buy
one stock and choosing a different day in the future to sell that
stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Example 1:
    Input: prices = [7, 1, 5, 3, 6, 4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5
    (price = 6), profit = 6 - 1 = 5. Note that buying on day 2
    and selling on day 1 is not allowed because you must buy
    before you sell.

Example 2:
    Input: prices = [7, 6, 4, 3, 1]
    Output: 0
    Explanation: In this case, no transactions are done and the
    max profit is 0.
"""


def max_profit(prices):
    """
    Return the maximum profit from one buy and one later sell.

    Approach: one pass with a sliding window whose left edge is
    the cheapest buying day seen so far. For each day as a selling
    day, the best profit using it is `price - min_price`. If the
    day's price is a new low, it becomes the new left edge --
    every earlier buy is worse, so the window restarts there.
    Otherwise the day is just a candidate sell, and the best
    profit is updated.

    Time complexity: O(n) -- a single pass over the prices.
    Space complexity: O(1) -- only the minimum price and the
    best profit are stored.
    """
    min_price = float("inf")
    best = 0
    for price in prices:
        if price < min_price:
            min_price = price
        else:
            best = max(best, price - min_price)
    return best


if __name__ == "__main__":
    # Classic example: buy at 1, sell at 6.
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    # Strictly falling prices: no profitable trade.
    assert max_profit([7, 6, 4, 3, 1]) == 0
    # Buy at the very start, sell at the very end.
    assert max_profit([1, 2, 3, 4, 5]) == 4
    # Best buy is not the first day; best sell is the last.
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4
    # Single day: no transaction possible.
    assert max_profit([5]) == 0
    # Flat prices: zero profit.
    assert max_profit([4, 4, 4, 4]) == 0
    print("All Best Time to Buy and Sell Stock tests passed!")

# Pattern notes:
# Sliding Window (minimum prefix): the window here is "buy day
# to sell day", and its left edge is simply the lowest price so
# far -- a new low restarts the window, because no earlier buy
# can beat it. The key insight is that the best pair is always
# (lowest price before a day, that day), so one pass tracking the
# running minimum is enough. Recognize this next time a problem
# asks for the biggest increase between two ordered elements:
# keep the best "before" value as you scan, and compare each new
# element against it.
