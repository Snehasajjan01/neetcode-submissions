class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq_1 = {}
        freq_2 = {}
        for num in nums1:
            freq_1[num] = freq_1.get(num,0) + 1
        for num in nums2:
            freq_2[num] = freq_2.get(num,0) + 1
        result = []
        for num in freq_1:
            if num in freq_2:
                result.append(num)
        return result
