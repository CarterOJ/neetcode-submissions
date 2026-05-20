class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set_s = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
        set_t = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}

        for i in s:
            set_s[i] += 1

        for i in t:
            set_t[i] += 1

        return set_s == set_t