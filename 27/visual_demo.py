"""
可视化演示双指针方法的工作过程
"""
class Solution(object):
    def removeElement(self, nums, val):
        left = 0
        
        print(f"\n开始处理: nums = {nums}, val = {val}")
        print(f"{'='*60}")
        
        for right in range(len(nums)):
            print(f"\n步骤 {right + 1}: right = {right}, nums[{right}] = {nums[right]}")
            print(f"当前数组: {nums}")
            
            # 可视化指针位置
            pointer_line = [' '] * (len(nums) * 4)
            if right < len(nums):
                pointer_line[right * 4] = 'R'  # Right pointer
            if left < len(nums):
                pointer_line[left * 4] = 'L'   # Left pointer
            print(f"指针位置: {''.join(pointer_line)}")
            print(f"          right={right}, left={left}")
            
            if nums[right] != val:
                print(f"  → nums[{right}] = {nums[right]} != {val}，保留此元素")
                print(f"  → 将 nums[{right}] 赋值给 nums[{left}]")
                nums[left] = nums[right]
                left += 1
                print(f"  → left 移动到 {left}")
                print(f"  → 数组变为: {nums}")
            else:
                print(f"  → nums[{right}] = {nums[right]} == {val}，跳过此元素")
                print(f"  → left 保持为 {left}")
        
        print(f"\n{'='*60}")
        print(f"处理完成！")
        print(f"返回 k = {left}")
        print(f"前 {left} 个元素: {nums[:left]}")
        print(f"完整数组: {nums}")
        
        return left


if __name__ == "__main__":
    solution = Solution()
    
    print("\n" + "="*60)
    print("示例 1: nums = [3, 2, 2, 3], val = 3")
    print("="*60)
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    
    print("\n\n" + "="*60)
    print("示例 2: nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2")
    print("="*60)
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)


