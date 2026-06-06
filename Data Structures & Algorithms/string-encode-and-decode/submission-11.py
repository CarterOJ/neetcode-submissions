class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs:
            return "\\e".join(strs) + "\\e"
        return ""

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        current_str = ""
        input_length = len(s)
        i = 0
        while i <= input_length - 1:
            if s[i] == "\\" and s[i+1] == "e":
                decoded_list.append(current_str)
                current_str = ""
                i += 2
            else:
                current_str += s[i]
                i += 1
        return decoded_list