class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 方法1：一次遍历（贪心算法，推荐）
        # 核心思想：记录最低买入价格，计算每天卖出的最大利润
        if not prices:
            return 0
        
        min_price = prices[0]  # 记录最低买入价格
        max_profit = 0  # 记录最大利润
        
        for price in prices[1:]:
            # 更新最大利润：当前价格 - 最低买入价格
            max_profit = max(max_profit, price - min_price)
            # 更新最低买入价格
            min_price = min(min_price, price)
        
        return max_profit
    
    def maxProfit_dp(self, prices):
        """
        方法2：动态规划
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        if not prices:
            return 0
        
        # dp[i][0] 表示第 i 天持有股票的最大利润
        # dp[i][1] 表示第 i 天不持有股票的最大利润
        hold = -prices[0]  # 持有股票（买入）
        not_hold = 0  # 不持有股票（卖出或未买入）
        
        for i in range(1, len(prices)):
            # 今天持有股票 = max(昨天持有, 今天买入)
            hold = max(hold, -prices[i])
            # 今天不持有股票 = max(昨天不持有, 今天卖出)
            not_hold = max(not_hold, hold + prices[i])
        
        return not_hold
    
    def maxProfit_bruteforce(self, prices):
        """
        方法3：暴力法（不推荐，仅用于理解）
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        max_profit = 0
        
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("方法1：一次遍历（贪心算法，推荐）")
    print("=" * 70)
    
    # 示例 1
    prices1 = [7, 1, 5, 3, 6, 4]
    result1 = solution.maxProfit(prices1)
    print(f"\n示例 1:")
    print(f"输入: prices = {prices1}")
    print(f"输出: {result1}")
    print(f"预期: 5")
    print(f"解释: 在第 2 天（价格=1）买入，在第 5 天（价格=6）卖出，利润 = 6-1 = 5")
    print(f"结果: {'正确' if result1 == 5 else '错误'}")
    
    # 示例 2
    prices2 = [7, 6, 4, 3, 1]
    result2 = solution.maxProfit(prices2)
    print(f"\n示例 2:")
    print(f"输入: prices = {prices2}")
    print(f"输出: {result2}")
    print(f"预期: 0")
    print(f"解释: 价格一直下跌，无法获得利润")
    print(f"结果: {'正确' if result2 == 0 else '错误'}")
    
    # 额外测试
    prices3 = [2, 4, 1]
    result3 = solution.maxProfit(prices3)
    print(f"\n额外测试:")
    print(f"输入: prices = {prices3}")
    print(f"输出: {result3}")
    print(f"预期: 2 (第1天买入价格2，第2天卖出价格4，利润=2)")
    print(f"结果: {'正确' if result3 == 2 else '错误'}")
    
    print("\n" + "=" * 70)
    print("方法2：动态规划")
    print("=" * 70)
    
    prices4 = [7, 1, 5, 3, 6, 4]
    result4 = solution.maxProfit_dp(prices4)
    print(f"\n输入: prices = {prices4}")
    print(f"输出: {result4}")
    print(f"预期: 5")
    print(f"结果: {'正确' if result4 == 5 else '错误'}")
    
    print("\n" + "=" * 70)
    print("算法复杂度对比：")
    print("=" * 70)
    print("方法1（一次遍历）: 时间 O(n), 空间 O(1) - 推荐")
    print("方法2（动态规划）: 时间 O(n), 空间 O(1)")
    print("方法3（暴力法）  : 时间 O(n^2), 空间 O(1) - 不推荐")
    
    print("\n" + "=" * 70)
    print("方法1执行过程演示（示例1）：")
    print("=" * 70)
    prices = [7, 1, 5, 3, 6, 4]
    min_price = prices[0]
    max_profit = 0
    print(f"初始: min_price = {min_price}, max_profit = {max_profit}\n")
    
    for i, price in enumerate(prices[1:], 1):
        old_min = min_price
        old_profit = max_profit
        max_profit = max(max_profit, price - min_price)
        min_price = min(min_price, price)
        print(f"第 {i+1} 天: price = {price}")
        print(f"  计算利润: {price} - {old_min} = {price - old_min}")
        print(f"  更新 max_profit: max({old_profit}, {price - old_min}) = {max_profit}")
        print(f"  更新 min_price: min({old_min}, {price}) = {min_price}\n")
    
    print(f"最终结果: {max_profit}")


