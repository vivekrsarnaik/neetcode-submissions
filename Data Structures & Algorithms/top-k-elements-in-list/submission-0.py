from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)  # Count how many times each number appears
        top_k = freq.most_common(k)  # Get the k most common (num, count) pairs
        return [num for num, count in top_k]  # Extract just the numbers