class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 方法1：贪心算法（推荐）
        # 核心思想：维护当前步数能到达的最远位置，当到达边界时增加步数
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0  # 跳跃次数
        max_reach = 0  # 当前能到达的最远位置
        end = 0  # 当前步数能到达的最远位置
        
        for i in range(n - 1):  # 不需要遍历最后一个位置
            # 更新能到达的最远位置
            max_reach = max(max_reach, i + nums[i])
            
            # 如果到达了当前步数的边界，需要增加一步
            if i == end:
                jumps += 1
                end = max_reach
                
                # 如果已经能到达最后一个位置，提前返回
                if end >= n - 1:
                    break
        
        return jumps
    
    def jump_alternative(self, nums):
        """
        方法2：另一种贪心思路
        从后往前找，每次找能到达当前位置的最远位置
        """
        n = len(nums)
        position = n - 1  # 目标位置
        steps = 0
        
        while position > 0:
            # 从前往后找能到达 position 的最远位置
            for i in range(position):
                if i + nums[i] >= position:
                    position = i
                    steps += 1
                    break
        
        return steps


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("方法1：贪心算法（推荐）")
    print("=" * 70)
    
    # 示例 1
    nums1 = [2, 3, 1, 1, 4]
    result1 = solution.jump(nums1)
    print(f"\n示例 1:")
    print(f"输入: nums = {nums1}")
    print(f"输出: {result1}")
    print(f"预期: 2")
    print(f"解释: 从下标 0 跳到下标 1（跳1步），然后从下标 1 跳3步到达最后一个位置")
    print(f"结果: {'正确' if result1 == 2 else '错误'}")
    
    # 示例 2
    nums2 = [2, 3, 0, 1, 4]
    result2 = solution.jump(nums2)
    print(f"\n示例 2:")
    print(f"输入: nums = {nums2}")
    print(f"输出: {result2}")
    print(f"预期: 2")
    print(f"结果: {'正确' if result2 == 2 else '错误'}")
    
    # 额外测试
    nums3 = [1]
    result3 = solution.jump(nums3)
    print(f"\n额外测试 1:")
    print(f"输入: nums = {nums3}")
    print(f"输出: {result3}")
    print(f"预期: 0 (只有一个元素，已经在最后一个位置)")
    print(f"结果: {'正确' if result3 == 0 else '错误'}")
    
    nums4 = [2, 1]
    result4 = solution.jump(nums4)
    print(f"\n额外测试 2:")
    print(f"输入: nums = {nums4}")
    print(f"输出: {result4}")
    print(f"预期: 1 (从下标0跳1步到下标1)")
    print(f"结果: {'正确' if result4 == 1 else '错误'}")
    
    print("\n" + "=" * 70)
    print("错误代码分析")
    print("=" * 70)
    
    print("""
错误代码：
    minstep = 0
    maxrea = 0
    
    if nums[0] < len(nums):
        for i in range(0, len(nums) - 1):
            if maxrea < i + nums[i] and i + nums[i] < len(nums):
                minstep += 1
            maxrea = max(maxrea, i + nums[i])
    
    return minstep

主要问题：

1. 【逻辑错误】条件判断 maxrea < i + nums[i] 不正确
   - 这个条件会在每次能扩展范围时都增加步数
   - 但实际上，我们应该在"到达当前步数的边界"时才增加步数
   - 例如：[2,3,1,1,4]
     * i=0: maxrea=0, 0+2=2, maxrea<2, minstep=1, maxrea=2
     * i=1: maxrea=2, 1+3=4, maxrea<4, minstep=2, maxrea=4
     * 结果：2（正确，但逻辑不对）
   - 但对于 [2,1,1,1,4]：
     * i=0: maxrea=0, 0+2=2, maxrea<2, minstep=1, maxrea=2
     * i=1: maxrea=2, 1+1=2, maxrea<2? 否，minstep=1, maxrea=2
     * i=2: maxrea=2, 2+1=3, maxrea<3, minstep=2, maxrea=3
     * 结果：2（但实际应该是2，这里碰巧对了）

2. 【边界条件错误】if nums[0] < len(nums) 没有意义
   - 如果 nums[0] >= len(nums)，代码直接返回 0
   - 但即使 nums[0] >= len(nums)，也应该能到达（一步就能到）
   - 例如：[5] 或 [10, 1, 1]，应该返回 1 或 0，而不是被这个条件限制

3. 【缺少边界检查】i + nums[i] < len(nums) 这个条件限制了跳跃
   - 实际上，如果 i + nums[i] >= len(nums)，说明能直接到达或超过最后一个位置
   - 这是好事，不应该被排除

4. 【初始值问题】没有处理数组长度为 1 的情况
   - 如果数组长度为 1，应该返回 0（已经在最后一个位置）
   - 但代码会进入循环，可能返回错误的值

正确的贪心算法思路：
------------------
1. 维护两个变量：
   - max_reach: 当前能到达的最远位置
   - end: 当前步数能到达的最远位置（边界）

2. 遍历数组（不需要遍历最后一个位置）：
   - 更新 max_reach = max(max_reach, i + nums[i])
   - 当 i == end 时，说明到达了当前步数的边界
   - 需要增加一步，并更新 end = max_reach

3. 如果 end >= n-1，提前返回

示例演示（正确算法）：
--------------------
nums = [2, 3, 1, 1, 4]

初始: jumps=0, max_reach=0, end=0

i=0: nums[0]=2
  max_reach = max(0, 0+2) = 2
  i == end? 是，jumps=1, end=2

i=1: nums[1]=3
  max_reach = max(2, 1+3) = 4
  i == end? 否（1 != 2），继续

i=2: nums[2]=1
  max_reach = max(4, 2+1) = 4
  i == end? 是（2 == 2），jumps=2, end=4
  end >= 4? 是，提前返回

结果: jumps = 2 (正确)
    """)
    
    print("\n" + "=" * 70)
    print("方法1执行过程演示（示例1）：")
    print("=" * 70)
    nums = [2, 3, 1, 1, 4]
    jumps = 0
    max_reach = 0
    end = 0
    print(f"初始: jumps={jumps}, max_reach={max_reach}, end={end}\n")
    
    for i in range(len(nums) - 1):
        print(f"位置 {i}: nums[{i}] = {nums[i]}")
        max_reach = max(max_reach, i + nums[i])
        print(f"  更新 max_reach: max({max_reach - nums[i] if i > 0 else 0}, {i} + {nums[i]}) = {max_reach}")
        
        if i == end:
            jumps += 1
            old_end = end
            end = max_reach
            print(f"  到达边界 i == end ({i} == {old_end})，增加步数: jumps = {jumps}")
            print(f"  更新边界: end = {end}")
            if end >= len(nums) - 1:
                print(f"  end ({end}) >= 最后一个位置 ({len(nums) - 1})，提前返回")
                break
        else:
            print(f"  未到达边界 (i={i} != end={end})，继续")
        print()

