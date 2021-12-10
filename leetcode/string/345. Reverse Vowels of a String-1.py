# 문자열에서 모음만 뒤집기
# 파이썬 다운
# 정규식

class Solution:
    def reverseVowels(self, s):
        vowels = re.findall('(?i)[aeiou]', s)
        return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
