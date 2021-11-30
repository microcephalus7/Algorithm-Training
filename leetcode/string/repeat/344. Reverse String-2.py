# for, len

class Solution:
    def reverseString(self, s: List[str]) -> None:
        string_length = len(s)

        for i in range(string_length//2):
            s[i], s[string_length-1-i] = s[string_length - 1 - i], s[i]
