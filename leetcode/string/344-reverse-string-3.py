# for len 이용

class Solution:
    def reverseString(self, s: List[str]) -> None:
        string_length = len(s)

        for index in range(string_length // 2):

            s[index], s[string_length - index -
                        1] = s[string_length - index - 1], s[index],
