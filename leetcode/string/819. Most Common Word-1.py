# 문장에서 가장 흔한 단어

# 정규식, counter, most_common

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()

        filterd_words = [word for word in words if word not in banned]

        counts = collections.Counter(filterd_words)

        return counts.most_common(1)[0][0]
