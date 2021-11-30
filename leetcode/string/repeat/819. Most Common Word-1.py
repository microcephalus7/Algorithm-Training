# 정규식, Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = re.sub(r'[^\w]', ' ', paragraph).lower().split()

        filtered_words = [word for word in words if word not in banned]

        return collections.Counter(filtered_words).most_common()[0][0]
