class Solution:
    # 1. O(n) t:48ms(13%) O(1) m:17.2M(?%) 遍历
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in letters:
            if letter > target:
                return letter
        return letters[0]
    
    # 2. O(logn) t:36ms(78%) O(1) m:16..9M(53%) 二分
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        r = bisect_right(letters, target)
        return letters[r] if r < len(letters) else letters[0]