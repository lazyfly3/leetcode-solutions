# 用户的错误代码
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i=len(nums)
        p=i-1
        numb=0
        if i>=0 and i<=100:
            while p>=0:
                if nums[p]!=val:
                    numb=numb + 1
                p = p-1
        return numb


# 测试用户的代码
if __name__ == "__main__":
    solution = Solution()
    
    # 示例 1
    nums1 = [3, 2, 2, 3]
    val1 = 3
    k1 = solution.removeElement(nums1, val1)
    print("=" * 50)
    print("示例 1 测试:")
    print(f"输入: nums = {nums1}, val = {val1}")
    print(f"返回的 k = {k1}")
    print(f"修改后的 nums = {nums1}")
    print(f"nums 的前 {k1} 个元素 = {nums1[:k1]}")
    print(f"问题：数组没有被修改！前 {k1} 个元素仍然是 [3, 2]，而不是 [2, 2]")
    
    # 示例 2
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    k2 = solution.removeElement(nums2, val2)
    print("\n" + "=" * 50)
    print("示例 2 测试:")
    print(f"输入: nums = {nums2}, val = {val2}")
    print(f"返回的 k = {k2}")
    print(f"修改后的 nums = {nums2}")
    print(f"nums 的前 {k2} 个元素 = {nums2[:k2]}")
    print(f"问题：数组没有被修改！前 {k2} 个元素仍然包含 val={val2} 的元素")

