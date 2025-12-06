class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 修正后的代码
        minstep = 0
        maxrea = 0
        end = 0  # 新增：当前步数能到达的最远位置（边界）
        
        # 修正1: 去掉 if nums[0] < len(nums) 这个条件，改为处理边界情况
        n = len(nums)
        if n <= 1:
            return 0
        
        # 修正2: 遍历到 n-1 即可（不需要遍历最后一个位置）
        for i in range(0, n - 1):
            # 修正3: 更新能到达的最远位置（这个是对的）
            maxrea = max(maxrea, i + nums[i])
            
            # 修正4: 改变条件判断逻辑
            # 原代码: if maxrea < i + nums[i] and i + nums[i] < len(nums):
            # 应该改为: 当到达当前步数的边界时，增加步数
            if i == end:  # 到达当前步数的边界
                minstep += 1
                end = maxrea  # 更新边界为能到达的最远位置
                
                # 修正5: 如果已经能到达最后一个位置，提前返回
                if end >= n - 1:
                    break
        
        return minstep

