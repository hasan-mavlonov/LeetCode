class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        counter = 0
        for word in strs:
            for letter in range(len(word)):
                prefix = word[letter] + word[letter + 1]
                if prefix in word:
                    counter += 1
                else:
                    counter = 0
        if counter == range(len(strs)):
            return 'Hello'


sol = Solution()
words = ['flower', 'flow', 'flower', 'flower', 'flower']
sol.longestCommonPrefix(words)
