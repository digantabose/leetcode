class Solution(object):
    def twoSum(self, num, target):
        seen = {}
        for i in range(len(num)):
            diff = target - num[i]
            if diff in seen:
                return [seen[diff], i]
            else: 
                seen[num[i]] = i
