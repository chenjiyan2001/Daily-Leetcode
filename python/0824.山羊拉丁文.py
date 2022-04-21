class Solution:
    # 1. O(k) t:36ms(66%) O(1) m:15M(49%) 模拟
    def toGoatLatin(self, sentence: str) -> str:
        vowel = ['a', 'e', 'i', 'o', 'u']
        ans = []
        for idx, word in enumerate(sentence.split(' ')):
            if word[0].lower() in vowel:
                ans.append(word + 'ma' + 'a' * (idx + 1))
            else:
                ans.append(word[1:] + word[0] + 'ma' + 'a' * (idx + 1))
        return ' '.join(ans)