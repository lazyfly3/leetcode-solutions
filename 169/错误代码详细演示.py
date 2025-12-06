"""
详细演示错误代码的执行过程和问题
"""

def wrong_majorityElement(nums):
    """
    错误代码的详细执行过程
    """
    print(f"\n输入数组: {nums}")
    k = len(nums)
    l = k/2
    print(f"k = {k}, l = k/2 = {l} (注意：这是浮点数)")
    print(f"range(l) = range({int(l)}) = {list(range(int(l)))}")
    print(f"只会检查前 {int(l)} 个元素\n")
    
    for i in range(int(l)):
        print(f"--- i = {i}, 检查元素 nums[{i}] = {nums[i]} ---")
        count = 0
        print(f"  j 从 1 到 {len(nums)-1}:")
        for j in range(1, len(nums)):
            print(f"    j = {j}, nums[{j}] = {nums[j]}", end="")
            if nums[i] == nums[j]:
                count += 1
                print(f" ✓ 匹配，count = {count}")
            else:
                print(f" ✗ 不匹配，count = {count}")
            # j += 1  # 这行代码无效，因为 j 会被循环自动更新
        print(f"  最终 count = {count}, k/2 = {k/2}")
        if count > k/2:
            print(f"  ✓ count > k/2，返回 nums[{i}] = {nums[i]}")
            return nums[i]
        else:
            print(f"  ✗ count <= k/2，继续下一个 i")
    print(f"\n所有 i 都检查完毕，没有找到多数元素，返回 None")
    return None


def correct_majorityElement(nums):
    """
    正确的解法：Boyer-Moore 投票算法
    """
    candidate = None
    count = 0
    
    print(f"\n正确解法（Boyer-Moore 投票算法）:")
    print(f"输入数组: {nums}\n")
    
    for num in nums:
        if count == 0:
            candidate = num
            print(f"  遇到 {num}，count=0，设置 candidate = {num}")
        count += (1 if num == candidate else -1)
        print(f"  遇到 {num}，count = {count}")
    
    print(f"\n最终 candidate = {candidate}")
    return candidate


if __name__ == "__main__":
    print("=" * 70)
    print("错误代码详细演示")
    print("=" * 70)
    
    # 示例 1
    print("\n【示例 1】")
    nums1 = [3, 2, 3]
    print(f"预期结果: 3 (出现2次，共3个元素，2 > 3/2 = 1.5)")
    result1_wrong = wrong_majorityElement(nums1)
    print(f"\n错误代码结果: {result1_wrong}")
    result1_correct = correct_majorityElement(nums1)
    print(f"正确代码结果: {result1_correct}")
    
    print("\n" + "=" * 70)
    
    # 示例 2
    print("\n【示例 2】")
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(f"预期结果: 2 (出现4次，共7个元素，4 > 7/2 = 3.5)")
    result2_wrong = wrong_majorityElement(nums2)
    print(f"\n错误代码结果: {result2_wrong}")
    result2_correct = correct_majorityElement(nums2)
    print(f"正确代码结果: {result2_correct}")
    
    print("\n" + "=" * 70)
    print("\n错误代码的主要问题总结：")
    print("1. k/2 是浮点数，range() 需要整数，应该用 k//2")
    print("2. 只遍历前 l 个元素，如果多数元素不在前 l 个，就找不到")
    print("3. j 从 1 开始，漏掉了索引 0，导致计数不准确")
    print("4. 计数逻辑错误：nums[i] 本身没有被正确计数")
    print("5. 如果多数元素不在前 l 个位置，函数返回 None")

