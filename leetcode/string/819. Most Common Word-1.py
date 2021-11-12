# 정규식, counter

# 정규식 이용하여 알파벳 아닌 문자 제거
# counter 생성
# most_common

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()

        filterd_words = [word for word in words if word not in banned]

        counts = collections.Counter(filterd_words)

        return counts.most_common(1)[0][0]
