# 문자열에서 찾는 글자 있으면 그 앞의 문자열까지 뒤집기

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                return word[:i + 1][::-1] + word[i + 1:]
        return word
