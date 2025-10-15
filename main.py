from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    a = {}
    for i, x in enumerate(nums):
        n = target - x
        if n in a:
            return [a[n], i]
        a[x] = i