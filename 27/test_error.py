# 用户的错误代码（会导致 IndexError）
class Solution(object):
    def removeElement(self, nums, val):
        i=len(nums)
        p=i-1
        numb=0
        if i>=0 and i<=100:
            while p>=0:
                if nums[p]!=val:
                    numb=numb + 1
                    p = p-1
                else:
                    # 问题代码：nums[p+1] 会越界
                    while nums[p+1]:  # IndexError: list index out of range
                        nums[p]=nums[p+1]
                    p=p-1                
        return numb


# 测试
if __name__ == "__main__":
    solution = Solution()
    nums = [3, 2, 2, 3]
    val = 3
    try:
        k = solution.removeElement(nums, val)
        print(f"k = {k}, nums = {nums}")
    except IndexError as e:
        print(f"错误: {e}")
        print("问题分析：")
        print("1. 当 p = i-1 时，p+1 = i，nums[i] 会越界")
        print("2. while nums[p+1]: 这个条件判断也不正确（0 也是有效值）")

