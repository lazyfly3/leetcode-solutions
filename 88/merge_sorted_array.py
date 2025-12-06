"""
合并两个有序数组

给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n，
分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。
为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，
后 n 个元素为 0，应忽略。nums2 的长度为 n。

时间复杂度：O(m + n)
空间复杂度：O(1)
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m - 1  # nums1 有效元素的最后一个索引
        j = n - 1  # nums2 的最后一个索引
        i = m + n - 1  # nums1 的最后一个索引（结果数组的末尾）
        
        # 从后往前合并
        # 注意：循环条件必须是 k>=0 and j>=0，不能是 i>=0 and j>=0
        # 因为当 k<0 时，说明 nums1 的有效元素已经处理完了，不应该再访问 nums1[k]
        while k >= 0 and j >= 0:
            if nums1[k] > nums2[j]:
                nums1[i] = nums1[k]
                k = k - 1
                i = i - 1
            else:
                nums1[i] = nums2[j]
                i = i - 1
                j = j - 1
        
        # 如果 nums2 还有剩余元素，需要继续填充
        while j >= 0:
            nums1[i] = nums2[j]
            j = j - 1
            i = i - 1
        
        # 注意：如果 nums1 还有剩余元素（k >= 0），不需要处理，
        # 因为它们已经在正确的位置上了


# 测试用例
if __name__ == "__main__":
    solution = Solution()
    
    # 示例 1
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"示例 1: {nums1}")  # 期望输出: [1, 2, 2, 3, 5, 6]
    
    # 示例 2
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    solution.merge(nums1, m, nums2, n)
    print(f"示例 2: {nums1}")  # 期望输出: [1]
    
    # 示例 3
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"示例 3: {nums1}")  # 期望输出: [1]
    
    # 额外测试用例：nums2 的所有元素都小于 nums1
    nums1 = [4, 5, 6, 0, 0, 0]
    m = 3
    nums2 = [1, 2, 3]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"额外测试 1: {nums1}")  # 期望输出: [1, 2, 3, 4, 5, 6]
    
    # 额外测试用例：nums1 的所有元素都小于 nums2
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [4, 5, 6]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"额外测试 2: {nums1}")  # 期望输出: [1, 2, 3, 4, 5, 6]
    
    # 额外测试用例：包含 0 作为有效元素
    nums1 = [-1, 0, 0, 3, 0, 0, 0]
    m = 4
    nums2 = [1, 2, 2]
    n = 3
    solution.merge(nums1, m, nums2, n)
    print(f"额外测试 3 (包含0): {nums1}")  # 期望输出: [-1, 0, 0, 1, 2, 2, 3]
    
    # 失败的测试用例：nums1=[2,0], m=1, nums2=[1], n=1
    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    solution.merge(nums1, m, nums2, n)
    print(f"失败用例修复: {nums1}")  # 期望输出: [1, 2]

