class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += string + "\\e"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        current_str = ""
        i = 0
        while i <= len(s) - 1:
            if s[i] == "\\" and s[i+1] == "e":
                decoded_list.append(current_str)
                current_str = ""
                i += 2
            else:
                current_str += s[i]
                i += 1
        return decoded_list