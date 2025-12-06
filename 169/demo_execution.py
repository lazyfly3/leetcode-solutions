"""
Boyer-Moore 投票算法的模拟运行流程演示
"""

def simulate_majority_element(nums):
    """
    模拟投票算法的执行过程
    """
    print("=" * 70)
    print(f"输入数组: {nums}")
    print(f"数组长度: {len(nums)}")
    print(f"多数元素需要出现次数 > {len(nums) // 2} 次")
    print("=" * 70)
    print("\n开始执行投票算法：\n")
    
    c, cnt = None, 0
    
    print(f"初始状态: candidate = {c}, count = {cnt}\n")
    print("-" * 70)
    
    for i, n in enumerate(nums):
        print(f"步骤 {i+1}: 处理元素 nums[{i}] = {n}")
        print(f"  当前状态: candidate = {c}, count = {cnt}")
        
        if not cnt:
            print(f"  -> count == 0，设置 candidate = {n}")
            c = n
            print(f"  更新后: candidate = {c}, count = {cnt}")
        else:
            print(f"  -> count != 0，继续使用当前 candidate = {c}")
        
        old_cnt = cnt
        if n == c:
            cnt += 1
            print(f"  -> {n} == {c}，count 从 {old_cnt} 增加到 {cnt} (+1)")
        else:
            cnt -= 1
            print(f"  -> {n} != {c}，count 从 {old_cnt} 减少到 {cnt} (-1)")
        
        print(f"  最终状态: candidate = {c}, count = {cnt}")
        print("-" * 70)
    
    print(f"\n算法执行完毕！")
    print(f"最终结果: candidate = {c}")
    print(f"最终 count = {cnt}")
    print("=" * 70)
    print()
    
    return c


if __name__ == "__main__":
    # 示例 1: [3, 2, 3]
    print("\n【示例 1】")
    nums1 = [3, 2, 3]
    result1 = simulate_majority_element(nums1)
    print(f"预期结果: 3")
    print(f"实际结果: {result1}")
    print(f"结果: {'正确' if result1 == 3 else '错误'}")
    
    # 示例 2: [2, 2, 1, 1, 1, 2, 2]
    print("\n\n【示例 2】")
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    result2 = simulate_majority_element(nums2)
    print(f"预期结果: 2")
    print(f"实际结果: {result2}")
    print(f"结果: {'正确' if result2 == 2 else '错误'}")
    
    # 示例 3: [1, 1, 1, 2, 2]
    print("\n\n【示例 3】")
    nums3 = [1, 1, 1, 2, 2]
    result3 = simulate_majority_element(nums3)
    print(f"预期结果: 1")
    print(f"实际结果: {result3}")
    print(f"结果: {'正确' if result3 == 1 else '错误'}")
    
    # 示例 4: [1]
    print("\n\n【示例 4】")
    nums4 = [1]
    result4 = simulate_majority_element(nums4)
    print(f"预期结果: 1")
    print(f"实际结果: {result4}")
    print(f"结果: {'正确' if result4 == 1 else '错误'}")


