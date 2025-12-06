class Solution(object):
    def majorityElement(self, nums):
        c, cnt = None, 0
        for n in nums:
            if not cnt:
                c = n
            cnt += 1 if n == c else -1
        return c

