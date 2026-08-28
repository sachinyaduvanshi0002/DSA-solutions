class Solution(object):
    def countStudents(self, students, sandwiches):
        cnt = 0

        while students:
            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                cnt = 0
                
            else:
                s = students.pop(0)
                students.append(s)
                cnt += 1

                if cnt == len(students): break

        return len(students)