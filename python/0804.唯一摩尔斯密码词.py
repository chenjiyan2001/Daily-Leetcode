class Solution:
    # 1. O(n) t:28ms(98%) O(n) m:15M(32%) 哈希
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {k:v for k, v in zip(range(26), [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."])}
        s = set()
        for word in words:
            s.add(''.join([d[ord(i) - ord('a')] for i in word]))
        return len(s)