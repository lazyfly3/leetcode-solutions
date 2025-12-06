class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        left = 0  # 指向下一个非 val 元素应该放置的位置
        
        for right in range(len(nums)):
            if nums[right] != val:
                nums[left] = nums[right]  # 将非 val 元素移到前面
                left += 1
        
        return left

