class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        """
        方法1：Boyer-Moore 投票算法（推荐）
        
        核心思想：
        - 多数元素的数量 > n/2，所以多数元素的数量 - 其他所有元素的数量 > 0
        - 使用候选人和计数器，遇到相同元素+1，遇到不同元素-1
        - 当计数器为0时，更换候选人
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        candidate = None  # 候选人
        count = 0  # 计数器
        
        # 第一遍遍历：找到可能的多数元素
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        # 由于题目保证一定存在多数元素，所以 candidate 就是答案
        # 如果不保证，需要第二遍遍历验证 candidate 是否真的是多数元素
        return candidate
    
    def majorityElement_hash(self, nums: list[int]) -> int:
        """
        方法2：哈希表统计
        
        使用字典统计每个元素出现的次数，返回出现次数最多的元素
        
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            if count[num] > len(nums) // 2:
                return num
        return -1  # 理论上不会执行到这里
    
    def majorityElement_sort(self, nums: list[int]) -> int:
        """
        方法3：排序后取中间值
        
        由于多数元素的数量 > n/2，排序后中间位置的元素一定是多数元素
        
        时间复杂度: O(n log n)
        空间复杂度: O(1) 或 O(n)，取决于排序算法
        """
        nums.sort()
        return nums[len(nums) // 2]


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 示例 1
    nums1 = [3, 2, 3]
    result1 = solution.majorityElement(nums1)
    print(f"示例 1: nums = {nums1}")
    print(f"输出: {result1}")
    print(f"预期: 3")
    print(f"结果: {'正确' if result1 == 3 else '错误'}\n")
    
    # 示例 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = solution.majorityElement(nums2)
    print(f"示例 2: nums = {nums2}")
    print(f"输出: {result2}")
    print(f"预期: 2")
    print(f"结果: {'正确' if result2 == 2 else '错误'}\n")
    
    # 测试其他方法
    print("=" * 50)
    print("测试其他解法：\n")
    
    print("方法2（哈希表）:")
    print(f"示例 1: {solution.majorityElement_hash(nums1)}")
    print(f"示例 2: {solution.majorityElement_hash(nums2)}")
    
    print("\n方法3（排序）:")
    print(f"示例 1: {solution.majorityElement_sort(nums1.copy())}")
    print(f"示例 2: {solution.majorityElement_sort(nums2.copy())}")
    
    # ============================================================
    # 错误代码分析
    # ============================================================
    print("\n" + "=" * 70)
    print("错误代码分析")
    print("=" * 70)
    
    print("""
错误代码：
class Solution(object):
    def majorityElement(self, nums):
        k = len(nums)
        l = k/2
        for i in range(l):
            count = 0
            for j in range(1, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
                    j += 1
            if count > k/2:
                return nums[i]

主要问题：

1. 【类型错误】k/2 是浮点数
   - 在 Python 3 中，k/2 返回浮点数（如 3/2 = 1.5）
   - range() 需要整数，所以 range(1.5) 会报错
   - 应该使用 k//2 进行整数除法

2. 【逻辑错误】只遍历前 l 个元素
   - range(l) 只检查前 l 个元素
   - 如果多数元素不在前 l 个位置，就找不到
   - 例如：[1, 1, 1, 2, 2]，多数元素是1，但如果1不在前2个位置就找不到

3. 【逻辑错误】j 从 1 开始，漏掉了索引 0
   - range(1, len(nums)) 从索引1开始
   - 当 i=0 时，nums[0] 本身没有被计数
   - 当 i>0 时，nums[i] 会被计数一次（当 j=i 时），但逻辑混乱

4. 【无效代码】j += 1 在 for 循环中无效
   - for 循环会自动更新 j
   - j += 1 这行代码没有任何作用

5. 【计数错误】计数逻辑不正确
   - 当 i=0 时，检查 nums[0]，但 j 从 1 开始
   - 所以 nums[0] 本身不会被计入 count
   - 例如：[3, 2, 3]，检查 nums[0]=3 时：
     * j=1: nums[1]=2 != 3, count=0
     * j=2: nums[2]=3 == 3, count=1
     * 最终 count=1，但实际 nums[0]=3 出现了2次（包括它自己）

6. 【返回值错误】可能返回 None
   - 如果多数元素不在前 l 个位置，函数没有返回值
   - 在 Python 中会返回 None，但题目保证有解

示例演示：

示例 1: [3, 2, 3]
- k=3, l=1.5, range(1.5) 会报错（实际会转换为 range(1) = [0]）
- i=0: 检查 nums[0]=3
  * j 从 1 到 2
  * j=1: nums[1]=2 != 3, count=0
  * j=2: nums[2]=3 == 3, count=1
  * count=1, k/2=1.5, 1 > 1.5? 否
- 没有找到，返回 None（错误！应该是 3）

正确的做法应该是：
- 使用 Boyer-Moore 投票算法（O(n) 时间，O(1) 空间）
- 或者使用哈希表统计（O(n) 时间，O(n) 空间）
- 或者排序后取中间值（O(n log n) 时间）
    """)

