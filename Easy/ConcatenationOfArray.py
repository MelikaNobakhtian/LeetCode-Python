# LeetCode 1929: Concatenation of Array
# Problem link: https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = []
        for _ in range(2):
            for num in nums:
                res.append(num)

        return res
        