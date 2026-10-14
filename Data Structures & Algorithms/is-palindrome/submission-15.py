class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalpha() or char.isnumeric()).lower()
        pointer_2 = len(s) - 1
        
        for i in range(len(s)):
            print("Pointers:", i, pointer_2)
            if i == pointer_2:
                return True
            elif s[i] != s[pointer_2]:
                return False

            pointer_2 -= 1

        return True