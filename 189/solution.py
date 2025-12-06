class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 方法1：三次反转法（推荐，O(1) 空间）
        n = len(nums)
        k = k % n  # 处理 k 大于数组长度的情况
        
        # 反转整个数组
        self._reverse(nums, 0, n - 1)
        # 反转前 k 个元素
        self._reverse(nums, 0, k - 1)
        # 反转后 n-k 个元素
        self._reverse(nums, k, n - 1)
    
    def _reverse(self, nums, start, end):
        """辅助函数：反转数组从 start 到 end 的部分"""
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate_extra_array(self, nums, k):
        """
        方法2：使用额外数组
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        n = len(nums)
        k = k % n
        result = [0] * n
        
        for i in range(n):
            result[(i + k) % n] = nums[i]
        
        nums[:] = result
    
    def rotate_cyclic(self, nums, k):
        """
        方法3：循环替换法（O(1) 空间）
        时间复杂度: O(n)
        空间复杂度: O(1)
        """
        n = len(nums)
        k = k % n
        
        if k == 0:
            return
        
        count = 0
        start = 0
        
        while count < n:
            current = start
            prev = nums[start]
            
            while True:
                next_idx = (current + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                current = next_idx
                count += 1
                
                if start == current:
                    break
            
            start += 1
    
    def rotate_slice(self, nums, k):
        """
        方法4：使用切片（Python 特性）
        时间复杂度: O(n)
        空间复杂度: O(n) - 切片会创建新数组
        """
        n = len(nums)
        k = k % n
        nums[:] = nums[-k:] + nums[:-k]


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("方法1：三次反转法（推荐）")
    print("=" * 70)
    
    # 示例 1
    nums1 = [1, 2, 3, 4, 5, 6, 7]
    k1 = 3
    print(f"\n示例 1:")
    print(f"输入: nums = {nums1}, k = {k1}")
    solution.rotate(nums1, k1)
    print(f"输出: {nums1}")
    print(f"预期: [5, 6, 7, 1, 2, 3, 4]")
    print(f"结果: {'正确' if nums1 == [5, 6, 7, 1, 2, 3, 4] else '错误'}")
    
    # 示例 2
    nums2 = [-1, -100, 3, 99]
    k2 = 2
    print(f"\n示例 2:")
    print(f"输入: nums = {nums2}, k = {k2}")
    solution.rotate(nums2, k2)
    print(f"输出: {nums2}")
    print(f"预期: [3, 99, -1, -100]")
    print(f"结果: {'正确' if nums2 == [3, 99, -1, -100] else '错误'}")
    
    print("\n" + "=" * 70)
    print("方法2：使用额外数组")
    print("=" * 70)
    
    nums3 = [1, 2, 3, 4, 5, 6, 7]
    k3 = 3
    print(f"\n输入: nums = {nums3}, k = {k3}")
    solution.rotate_extra_array(nums3, k3)
    print(f"输出: {nums3}")
    
    print("\n" + "=" * 70)
    print("方法3：循环替换法")
    print("=" * 70)
    
    nums4 = [1, 2, 3, 4, 5, 6, 7]
    k4 = 3
    print(f"\n输入: nums = {nums4}, k = {k4}")
    solution.rotate_cyclic(nums4, k4)
    print(f"输出: {nums4}")
    
    print("\n" + "=" * 70)
    print("方法4：使用切片")
    print("=" * 70)
    
    nums5 = [1, 2, 3, 4, 5, 6, 7]
    k5 = 3
    print(f"\n输入: nums = {nums5}, k = {k5}")
    solution.rotate_slice(nums5, k5)
    print(f"输出: {nums5}")
    
    print("\n" + "=" * 70)
    print("算法复杂度对比：")
    print("=" * 70)
    print("方法1（三次反转）: 时间 O(n), 空间 O(1) - 推荐")
    print("方法2（额外数组）: 时间 O(n), 空间 O(n)")
    print("方法3（循环替换）: 时间 O(n), 空间 O(1)")
    print("方法4（切片）    : 时间 O(n), 空间 O(n)")


