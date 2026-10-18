class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}

        for i, num in enumerate(nums):
            req_no = target - num

            if req_no in seen:
                return [seen[req_no], i]

            seen[num] = i