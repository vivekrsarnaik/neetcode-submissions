class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        found = False
        for n in nums:
            if n in seen:
                return True
                break
            seen.add(n)
        return False

        