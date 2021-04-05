# Before start, I practice for loop and while loop again with Udemy course.

student_heights = input("Please input student heights.\n").split()
for i in range(0, len(student_heights)):
    student_heights[i] = int(student_heights[i])

total_height = 0
for height in student_heights:
    total_height += height
print("Total height is", total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print("Total number of students is", number_of_students)
average_height = total_height / number_of_students
print("The average is", round(average_height, 1))

highest_value = 0
for height in student_heights:
    if height > highest_value:
        highest_value = height
print("The highest value is", highest_value)

total = 0
for number in range(1, 101):
    total += number

print(total)
