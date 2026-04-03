def countStudents(students, sandwiches):
    count_0 = students.count(0)
    count_1 = students.count(1)
    for sandwich in sandwiches:
        if sandwich == 0:
            if count_0 > 0:
                count_0 -= 1
            else:
                break
        else:  # sandwich == 1
            if count_1 > 0:
                count_1 -= 1
            else:
                break
    return count_0 + count_1

print(countStudents([1, 1, 0, 0], [0, 1, 0, 1]))
print(countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]))