# defaultdict

class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        log_dict = collections.defaultdict(set)

        output = [0] * k

        for (people, action) in logs:
            log_dict[people].add(action)

        for i in log_dict:
            output[len(log_dict[i]) - 1] += 1

        return output
