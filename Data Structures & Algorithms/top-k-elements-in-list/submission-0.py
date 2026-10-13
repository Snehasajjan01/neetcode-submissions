class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        count = 0
        nums.sort()
        arr = nums
        for num in nums:
            map[num] = map.get(num,0) + 1
       
        sorted_nums = sorted(map, key=lambda num:map[num],reverse = True)
        return sorted_nums[:k]

        