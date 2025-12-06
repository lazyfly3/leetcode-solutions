"""
分析错误代码的问题
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        错误代码分析
        """
        k = len(nums)
        l = k/2  # 问题1: Python 3中 / 是浮点除法，应该是 k//2
        for i in range(l):  # 问题2: 只遍历前 l 个元素，可能漏掉多数元素
            count = 0
            for j in range(1, len(nums)):  # 问题3: j从1开始，漏掉了索引0
                if nums[i] == nums[j]:
                    count += 1
                    j += 1  # 问题4: 这个语句无效，j会被循环自动更新
            if count > k/2:  # 问题5: 同样的问题，应该是 k//2
                return nums[i]
        # 问题6: 如果没有找到，函数返回None，但题目保证有解

# 测试错误代码
def test_wrong_code():
    solution = Solution()
    
    print("=" * 60)
    print("测试错误代码的问题：\n")
    
    # 示例 1: [3, 2, 3]
    nums1 = [3, 2, 3]
    print(f"示例 1: nums = {nums1}")
    print(f"k = {len(nums1)}, l = {len(nums1)/2} = {len(nums1)//2}")
    print(f"range(l) = range({len(nums1)//2}) = [0]")
    print("i=0: 检查 nums[0]=3")
    print("  j 从 1 到 2:")
    print("    j=1: nums[1]=2 != 3, count=0")
    print("    j=2: nums[2]=3 == 3, count=1")
    print("  count=1, k/2=1.5, 1 > 1.5? 否")
    print(f"结果: {solution.majorityElement(nums1)}")
    print("问题: 只检查了 nums[0]，但 nums[0] 本身没有被正确计数\n")
    
    # 示例 2: [2, 2, 1, 1, 1, 2, 2]
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(f"示例 2: nums = {nums2}")
    print(f"k = {len(nums2)}, l = {len(nums2)/2} = {len(nums2)//2}")
    print(f"range(l) = range({len(nums2)//2}) = [0, 1, 2]")
    print("只检查前3个元素，但多数元素2在后面的位置也有")
    result2 = solution.majorityElement(nums2)
    print(f"结果: {result2}")
    print("问题: 可能返回None或错误答案\n")
    
    print("=" * 60)
    print("错误代码的主要问题：\n")
    print("1. k/2 在 Python 3 中是浮点数，应该用 k//2")
    print("2. 只遍历前 l 个元素，可能漏掉多数元素")
    print("3. j 从 1 开始，漏掉了索引 0 的元素")
    print("4. j += 1 在 for 循环中无效")
    print("5. count 的计数逻辑错误：")
    print("   - 当 i=0 时，nums[0] 本身没有被计数")
    print("   - 当 i>0 时，nums[i] 会被计数一次（当 j=i 时）")
    print("   - 但整体计数逻辑混乱")
    print("6. 如果没有找到多数元素，函数返回 None")


if __name__ == "__main__":
    test_wrong_code()

