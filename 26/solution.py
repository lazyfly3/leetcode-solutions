class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        # 使用双指针方法
        # slow 指向下一个应该写入的位置（已去重数组的末尾）
        # fast 遍历整个数组
        slow = 0
        
        for fast in range(len(nums)):
            # 判断条件：
            # 1. slow < 2：前两个元素总是可以保留
            # 2. nums[fast] != nums[slow-2]：当前元素与 slow-2 位置的元素不同
            #    说明当前元素不会导致某个数字出现超过2次
            if slow < 2 or nums[fast] != nums[slow - 2]:
                nums[slow] = nums[fast]
                slow += 1
        
        # 返回去重后数组的长度
        return slow

