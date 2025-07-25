# ------Activity 5 --------

Student_data = {"Arun": 90, "Dilip": 60, "Kailash": 95, "Govind": 96}

user_input = input("Enter the student's name: ")

if user_input in Student_data:
    marks = Student_data[user_input]
    print("{} marks: {}".format(user_input, marks))
else:
    print("Student not found")


number_list = [1,2,3,4,5,6,7,8,9,10]

First_Five = number_list[0:5]
Rever_list = First_Five[::-1] 

print("Original list:", number_list)
print("Extracted first five elements:", First_Five)
print("Reversed extracted elements:", Rever_list)


