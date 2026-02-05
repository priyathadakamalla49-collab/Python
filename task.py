#  Practice – 20 Questions
# Given Dictionary:
student = {
    "name": "Ravi",
    "age": 20,
    "course": "Python",
    "marks": 85
}
# 1. Add a new key 'city' with value 'Hyderabad'.
student['city'] = 'Hyderabad'
# 2. Add a key 'email' with any email address.
student['email'] = 'r@gmail.com'
# 3. Add a key 'phone' with value 9876543210.
student['phone'] = 9876543210
# 4. Add keys 'college' and 'year' in one statement.
student.update({'college' : '10K','Year':2025})
# 5. Print the value of the key 'name'.
print(student['name'])
# 6. Print the value of the key 'marks'.
print(student['marks'])
# 7. Print all keys in the dictionary.
print(student.keys())
# 8. Print all values in the dictionary.
print(student.values())
# 9. Update the value of 'marks' to 90.
student['marks'] = 90
# 10. Increase the value of 'age' by 1.
for i in student.keys():
    if i == 'age':
        student['age'] +=1
print(student['age'])
# 11. Change the value of 'course' to 'Data Science'.
student['course'] = 'Data Science'
# 12. Remove the key 'email' using pop().
student.pop('email')
# 13. Remove the last inserted key-value pair using popitem().
student.popitem()
# 14. Clear the entire dictionary.
student.clear()
# 15. Guess the output:
#    student['marks'] = 95
#    print(student['marks'])
95
# 16. Guess the output:
#    student.pop('age')
#    print(student)
{'name': 'ravi','course':'Data Science','marks':90,'city':'Hyderabad','email':'r@gmail.com','phone':9876543210,'college':'10k','year':2025}
# 17. Guess the output:
# print('course' in student)
True
# 18. Guess the output :
#    print(student.get('city', 'Hyderabad'))
'Hyderabad'
# 19. Guess the output:
#    student.clear()
#    print(len(student))
0
# 20. Guess the output:
#    print(student.get('email'))
if it is not exist -- None
print(student)
