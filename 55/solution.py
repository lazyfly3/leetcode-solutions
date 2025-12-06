class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 方法1：贪心算法（推荐）
        # 核心思想：维护能到达的最远位置，如果最远位置 >= 最后一个下标，返回 true
        max_reach = 0  # 当前能到达的最远位置
        
        for i in range(len(nums)):
            # 如果当前位置超过了能到达的最远位置，说明无法到达
            if i > max_reach:
                return False
            
            # 更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果已经能到达最后一个下标，提前返回
            if max_reach >= len(nums) - 1:
                return True
        
        return True
    
    def canJump_dp(self, nums):
        """
        方法2：动态规划（从后往前）
        时间复杂度: O(n^2)
        空间复杂度: O(n)
        """
        n = len(nums)
        dp = [False] * n
        dp[n - 1] = True  # 最后一个位置肯定能到达
        
        # 从后往前遍历
        for i in range(n - 2, -1, -1):
            # 检查从位置 i 能否到达最后一个位置
            for j in range(i + 1, min(i + nums[i] + 1, n)):
                if dp[j]:
                    dp[i] = True
                    break
        
        return dp[0]
    
    def canJump_greedy_optimized(self, nums):
        """
        方法3：优化的贪心算法
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            # 如果当前位置超过了能到达的最远位置，返回 False
            if i > max_reach:
                return False
            
            # 更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])
        
        # 检查是否能到达最后一个位置
        return max_reach >= n - 1


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("方法1：贪心算法（推荐）")
    print("=" * 70)
    
    # 示例 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.canJump(nums1)
    print(f"\n示例 1:")
    print(f"输入: nums = {nums1}")
    print(f"输出: {result1}")
    print(f"预期: True")
    print(f"解释: 从下标 0 跳 1 步到下标 1，然后从下标 1 跳 3 步到达最后一个下标")
    print(f"结果: {'正确' if result1 == True else '错误'}")
    
    # 示例 2
    nums2 = [3, 2, 1, 0, 4]
    result2 = solution.canJump(nums2)
    print(f"\n示例 2:")
    print(f"输入: nums = {nums2}")
    print(f"输出: {result2}")
    print(f"预期: False")
    print(f"解释: 无论怎样都会到达下标 3，但该位置最大跳跃长度是 0，无法继续")
    print(f"结果: {'正确' if result2 == False else '错误'}")
    
    # 额外测试
    nums3 = [0]
    result3 = solution.canJump(nums3)
    print(f"\n额外测试 1:")
    print(f"输入: nums = {nums3}")
    print(f"输出: {result3}")
    print(f"预期: True (只有一个元素，已经在最后一个位置)")
    print(f"结果: {'正确' if result3 == True else '错误'}")
    
    nums4 = [2, 0, 0]
    result4 = solution.canJump(nums4)
    print(f"\n额外测试 2:")
    print(f"输入: nums = {nums4}")
    print(f"输出: {result4}")
    print(f"预期: True (从下标 0 跳 2 步直接到达最后一个下标)")
    print(f"结果: {'正确' if result4 == True else '错误'}")
    
    print("\n" + "=" * 70)
    print("方法2：动态规划")
    print("=" * 70)
    
    nums5 = [2, 3, 1, 1, 4]
    result5 = solution.canJump_dp(nums5)
    print(f"\n输入: nums = {nums5}")
    print(f"输出: {result5}")
    print(f"预期: True")
    print(f"结果: {'正确' if result5 == True else '错误'}")
    
    print("\n" + "=" * 70)
    print("算法复杂度对比：")
    print("=" * 70)
    print("方法1（贪心算法）    : 时间 O(n), 空间 O(1) - 推荐")
    print("方法2（动态规划）    : 时间 O(n^2), 空间 O(n)")
    print("方法3（优化贪心）    : 时间 O(n), 空间 O(1)")
    
    print("\n" + "=" * 70)
    print("方法1执行过程演示（示例1）：")
    print("=" * 70)
    nums = [2, 3, 1, 1, 4]
    max_reach = 0
    print(f"初始: max_reach = {max_reach}\n")
    
    for i in range(len(nums)):
        print(f"位置 {i}: nums[{i}] = {nums[i]}")
        print(f"  当前位置 {i} <= max_reach ({max_reach})? {'是' if i <= max_reach else '否'}")
        
        if i > max_reach:
            print(f"  -> 无法到达位置 {i}，返回 False")
            break
        
        old_max = max_reach
        max_reach = max(max_reach, i + nums[i])
        print(f"  更新 max_reach: max({old_max}, {i} + {nums[i]}) = {max_reach}")
        
        if max_reach >= len(nums) - 1:
            print(f"  -> max_reach ({max_reach}) >= 最后一个位置 ({len(nums) - 1})，可以到达！")
            break
        print()
    
    print("\n" + "=" * 70)
    print("方法1执行过程演示（示例2）：")
    print("=" * 70)
    nums = [3, 2, 1, 0, 4]
    max_reach = 0
    print(f"初始: max_reach = {max_reach}\n")
    
    for i in range(len(nums)):
        print(f"位置 {i}: nums[{i}] = {nums[i]}")
        print(f"  当前位置 {i} <= max_reach ({max_reach})? {'是' if i <= max_reach else '否'}")
        
        if i > max_reach:
            print(f"  -> 无法到达位置 {i}，返回 False")
            break
        
        old_max = max_reach
        max_reach = max(max_reach, i + nums[i])
        print(f"  更新 max_reach: max({old_max}, {i} + {nums[i]}) = {max_reach}")
        print()

