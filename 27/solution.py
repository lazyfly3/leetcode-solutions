class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        """
        移除数组中所有等于 val 的元素，并返回剩余元素的数量
        
        使用双指针方法：
        - left: 指向下一个应该放置非 val 元素的位置
        - right: 遍历整个数组
        
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        left = 0  # 慢指针，指向下一个非 val 元素应该放置的位置
        
        # 快指针 right 遍历整个数组
        for right in range(len(nums)):
            # 如果当前元素不等于 val，将其放到 left 位置
            if nums[right] != val:
                nums[left] = nums[right]
                left += 1
        
        return left


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    # 示例 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print(f"示例 1: k = {k1}, nums 前 {k1} 个元素 = {nums1[:k1]}")
    print(f"完整数组: {nums1}")
    
    # 示例 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print(f"\n示例 2: k = {k2}, nums 前 {k2} 个元素 = {nums2[:k2]}")
    print(f"完整数组: {nums2}")

