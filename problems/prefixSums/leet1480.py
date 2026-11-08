class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = nums

        for i in range(1, len(nums)):
            r[i] += r[i-1]

        return r