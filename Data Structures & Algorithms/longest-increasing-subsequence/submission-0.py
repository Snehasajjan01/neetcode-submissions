class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
        maxIndex = 0
        for i in range(len(dp)):
            if dp[i] > dp[maxIndex]:
                maxIndex = i
        return dp[maxIndex] + 1


        