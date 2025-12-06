class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 方法 1：双指针（推荐）
        left = 0  # 指向下一个非 val 元素应该放置的位置
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]  # 将非 val 元素移到前面
                left += 1
        
        return left


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 示例 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(f"示例 1:")
    print(f"输入: nums = {nums1}, val = {val1}")
    k1 = solution.removeElement(nums1, val1)
    print(f"输出: k = {k1}, nums 前 {k1} 个元素 = {nums1[:k1]}")
    print(f"完整数组: {nums1}")
    
    # 示例 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(f"\n示例 2:")
    print(f"输入: nums = {nums2}, val = {val2}")
    k2 = solution.removeElement(nums2, val2)
    print(f"输出: k = {k2}, nums 前 {k2} 个元素 = {nums2[:k2]}")
    print(f"完整数组: {nums2}")
    
    # 边界情况：包含 0 的情况
    nums3 = [0, 1, 0, 3, 0]
    val3 = 0
    print(f"\n边界情况（包含 0）:")
    print(f"输入: nums = {nums3}, val = {val3}")
    k3 = solution.removeElement(nums3, val3)
    print(f"输出: k = {k3}, nums 前 {k3} 个元素 = {nums3[:k3]}")
    print(f"完整数组: {nums3}")

