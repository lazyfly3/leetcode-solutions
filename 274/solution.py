class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 方法1：排序后遍历（推荐）
        citations.sort(reverse=True)  # 从大到小排序
        
        h = 0
        for i in range(len(citations)):
            # 如果第 i+1 篇论文的引用次数 >= i+1，则 h 至少为 i+1
            if citations[i] >= i + 1:
                h = i + 1
            else:
                break
        
        return h
    
    def hIndex_counting(self, citations):
        """
        方法2：计数排序（适用于 citations 值较小的情况）
        时间复杂度: O(n)
        空间复杂度: O(n)
        """
        n = len(citations)
        # 创建一个数组，count[i] 表示引用次数为 i 的论文数量
        # 对于引用次数 >= n 的，都算作 n
        count = [0] * (n + 1)
        
        for c in citations:
            if c >= n:
                count[n] += 1
            else:
                count[c] += 1
        
        # 从后往前累加，找到最大的 h
        papers = 0
        for i in range(n, -1, -1):
            papers += count[i]
            if papers >= i:
                return i
        
        return 0
    
    def hIndex_bruteforce(self, citations):
        """
        方法3：暴力法（用于理解）
        时间复杂度: O(n^2)
        空间复杂度: O(1)
        """
        n = len(citations)
        h = 0
        
        # 尝试所有可能的 h 值（从 0 到 n）
        for candidate_h in range(n + 1):
            count = 0
            # 统计有多少篇论文引用次数 >= candidate_h
            for c in citations:
                if c >= candidate_h:
                    count += 1
            # 如果至少有 candidate_h 篇论文引用次数 >= candidate_h
            if count >= candidate_h:
                h = candidate_h
        
        return h


# 测试代码
if __name__ == "__main__":
    solution = Solution()
    
    print("=" * 70)
    print("方法1：排序后遍历（推荐）")
    print("=" * 70)
    
    # 示例 1
    citations1 = [3, 0, 6, 1, 5]
    result1 = solution.hIndex(citations1)
    print(f"\n示例 1:")
    print(f"输入: citations = {citations1}")
    print(f"输出: {result1}")
    print(f"预期: 3")
    print(f"解释: 有 3 篇论文每篇至少被引用了 3 次")
    print(f"结果: {'正确' if result1 == 3 else '错误'}")
    
    # 示例 2
    citations2 = [1, 3, 1]
    result2 = solution.hIndex(citations2)
    print(f"\n示例 2:")
    print(f"输入: citations = {citations2}")
    print(f"输出: {result2}")
    print(f"预期: 1")
    print(f"结果: {'正确' if result2 == 1 else '错误'}")
    
    # 额外测试
    citations3 = [0]
    result3 = solution.hIndex(citations3)
    print(f"\n额外测试 1:")
    print(f"输入: citations = {citations3}")
    print(f"输出: {result3}")
    print(f"预期: 0")
    print(f"结果: {'正确' if result3 == 0 else '错误'}")
    
    citations4 = [100]
    result4 = solution.hIndex(citations4)
    print(f"\n额外测试 2:")
    print(f"输入: citations = {citations4}")
    print(f"输出: {result4}")
    print(f"预期: 1 (有 1 篇论文被引用 100 次，所以 h=1)")
    print(f"结果: {'正确' if result4 == 1 else '错误'}")
    
    print("\n" + "=" * 70)
    print("错误代码分析")
    print("=" * 70)
    
    print("""
错误代码：
    h = 0
    temh = 0
    m = len(citations) - 1
    
    for i in range(0, m):
        num = 0
        if citations[i] < len(citations): 
            for k in range(0, m):
                if citations[k] >= citations[i]:
                    num += 1
            if num >= citations[i]:
                temh = max(temh, citations[i])
    
    return temh

主要问题：

1. 【范围错误】range(0, m) 漏掉了最后一个元素
   - m = len(citations) - 1
   - range(0, m) 只遍历到倒数第二个元素
   - 应该用 range(len(citations)) 或 range(0, len(citations))

2. 【条件判断错误】if citations[i] < len(citations) 没有意义
   - 这个条件限制了只考虑引用次数 < 数组长度的论文
   - 但 h 指数可能等于数组长度（例如 [100] 的 h=1）
   - 应该考虑所有可能的 h 值

3. 【逻辑错误】只考虑 citations 中的值作为 h
   - h 指数不一定是 citations 中的某个值
   - 例如：[1, 3, 1] 的 h=1，但应该考虑所有可能的 h 值
   - 应该尝试从 0 到 n 的所有可能的 h 值

4. 【双重循环效率低】时间复杂度 O(n^2)
   - 可以用排序优化到 O(n log n)
   - 或者用计数排序优化到 O(n)

5. 【边界情况】没有处理空数组或特殊情况
   - 如果数组为空，应该返回 0

正确的思路：
----------
方法1（排序）：
1. 将数组从大到小排序
2. 遍历排序后的数组
3. 如果第 i+1 篇论文的引用次数 >= i+1，则 h 至少为 i+1
4. 找到最大的满足条件的 h

方法2（计数排序）：
1. 统计每个引用次数的论文数量
2. 从大到小累加，找到最大的 h 使得至少有 h 篇论文引用次数 >= h

示例演示（正确算法）：
--------------------
citations = [3, 0, 6, 1, 5]

排序后: [6, 5, 3, 1, 0]

i=0: citations[0]=6 >= 1? 是，h=1
i=1: citations[1]=5 >= 2? 是，h=2
i=2: citations[2]=3 >= 3? 是，h=3
i=3: citations[3]=1 >= 4? 否，停止

结果: h = 3 (正确)
    """)
    
    print("\n" + "=" * 70)
    print("方法1执行过程演示（示例1）：")
    print("=" * 70)
    citations = [3, 0, 6, 1, 5]
    print(f"原数组: {citations}")
    citations_sorted = sorted(citations, reverse=True)
    print(f"排序后: {citations_sorted}\n")
    
    h = 0
    for i in range(len(citations_sorted)):
        print(f"位置 {i}: citations[{i}] = {citations_sorted[i]}")
        if citations_sorted[i] >= i + 1:
            h = i + 1
            print(f"  {citations_sorted[i]} >= {i + 1}? 是，更新 h = {h}")
        else:
            print(f"  {citations_sorted[i]} >= {i + 1}? 否，停止")
            break
        print()
    
    print(f"最终结果: h = {h}")

