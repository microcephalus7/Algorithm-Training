# deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students = collections.deque(students)
        sandwiches = collections.deque(sandwiches)

        while sandwiches and students.count(sandwiches[0]) != 0:
            if sandwiches[0] == students[0]:
                students.popleft()
                sandwiches.popleft()
            else:
                students.append(students.popleft())

        return len(students)
