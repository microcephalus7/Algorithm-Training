# counter

class Solution:
    def countStudents(self, students, sandwiches):
        count = collections.Counter(students)
        students_len, sandwiches_index = len(students), 0
        while sandwiches_index < students_len and count[sandwiches[sandwiches_index]]:
            count[sandwiches[sandwiches_index]] -= 1
            sandwiches_index += 1
        return students_len - sandwiches_index
