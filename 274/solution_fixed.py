class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # 修正后的代码（保持原有结构，但修正关键错误）
        h = 0
        temh = 0
        n = len(citations)
        
        # 修正1: 处理边界情况
        if n == 0:
            return 0
        
        # 修正2: 遍历所有元素，不要用 m = len(citations) - 1
        # 原代码: m = len(citations) - 1, for i in range(0, m)
        # 改为: 遍历所有元素
        for i in range(0, n):
            num = 0
            # 修正3: 去掉 if citations[i] < len(citations) 这个限制条件
            # 这个条件没有意义，应该去掉
            
            # 修正4: 统计有多少篇论文引用次数 >= citations[i]
            for k in range(0, n):  # 修正: 遍历所有元素，不要用 m
                if citations[k] >= citations[i]:
                    num += 1
            
            # 修正5: 如果至少有 citations[i] 篇论文引用次数 >= citations[i]
            if num >= citations[i]:
                temh = max(temh, citations[i])
        
        return temh
    
    def hIndex_better(self, citations):
        """
        更好的修正版本：考虑所有可能的 h 值（不仅仅是 citations 中的值）
        """
        n = len(citations)
        if n == 0:
            return 0
        
        temh = 0
        # 尝试所有可能的 h 值（从 0 到 n）
        for candidate_h in range(n + 1):
            num = 0
            # 统计有多少篇论文引用次数 >= candidate_h
            for k in range(n):
                if citations[k] >= candidate_h:
                    num += 1
            # 如果至少有 candidate_h 篇论文引用次数 >= candidate_h
            if num >= candidate_h:
                temh = max(temh, candidate_h)
        
        return temh

