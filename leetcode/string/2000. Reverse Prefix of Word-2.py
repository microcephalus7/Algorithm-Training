# 문자열에서 찾는 글자 있으면 그 앞의 문자열까지 뒤집기
# find

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        idx = word.find(ch)

        return word[:idx+1][::-1] + word[idx+1:]
