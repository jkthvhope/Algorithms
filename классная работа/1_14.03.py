def maxProfit_cw(prices):
    l, r = 0, 1 # l - покупка, r - продажа
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            tekysh_profit = prices[r] - prices[l]
            max_profit = max(max_profit, tekysh_profit)
        else:
            l = r
        r += 1
    return max_profit

prices1 = [7]
print(maxProfit_cw(prices1))

prices2 = [7,6,4,3,1]
print(maxProfit_cw(prices2))