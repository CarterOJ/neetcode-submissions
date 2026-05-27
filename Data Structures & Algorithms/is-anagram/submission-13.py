class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha_s = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        alpha_t = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for char in s:
            alpha_s[char] += 1

        for char in t:
            alpha_t[char] += 1

        return alpha_s == alpha_t