from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hset = set()

        for n in nums:
            if n in hset:
                return True
            hset.add(n)
        return False    

if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 2, 3, 4], False),
        ([1, 2, 3, 1], True),
        ([1, 1, 1, 1], True),
        ([], False),
        ([1], False)
    ]
    
    for nums, expected in test_cases:
        result = solution.containsDuplicate(nums)
        print(f"containsDuplicate({nums}) = {result}, expected = {expected}")            