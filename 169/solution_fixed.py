class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = len(nums)
        # 修正1: 移除未使用的变量 l
        
        # 修正2: 遍历所有元素（这个是对的）
        for i in range(0, len(nums)):
            count = 0
            # 修正3: j 应该从 0 开始，这样才能正确计数 nums[i] 本身
            # 或者：j 从 0 开始，包含 i，这样 nums[i] 会被计数一次
            for j in range(0, len(nums)):
                if nums[i] == nums[j]:
                    count += 1
            
            # 修正4: 使用整数比较，count > k//2 或者 count >= k//2 + 1
            # 因为多数元素数量 > n/2，所以 count >= k//2 + 1
            if count > k // 2:
                return nums[i]
        
        # 理论上不会执行到这里，因为题目保证有解
        return None

