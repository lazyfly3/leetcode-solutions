class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        
        for i in range(0, len(nums)):
            count = 0
            # 修正：j 从 0 开始，这样才能正确计数 nums[i] 本身
            for j in range(0, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            
            # 修正：使用整数除法 k//2
            if count > k // 2:
                return nums[i]
        
        return None


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
    
    print("修正说明：")
    print("1. 移除了未使用的变量 l")
    print("2. j 从 0 开始（而不是从 1 开始），这样才能正确计数 nums[i] 本身")
    print("3. 使用 k//2 进行整数比较（而不是 k/2 浮点数）")

