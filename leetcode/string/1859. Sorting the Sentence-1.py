# 정규식

class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()

        s.sort(key=lambda x: re.sub('[^0-9]', '', x))

        s = [re.sub('[^a-zA-Z]', '', i) for i in s]

        return ' '.join(s)
