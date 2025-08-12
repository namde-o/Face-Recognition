# Step 1: Create a list (array) of numbers
marks = [85, 90, 78, 92, 88]  # Example: marks of 5 students

# Step 2: Print the list
print("Marks:", marks)

# Step 3: Access an element (index starts from 0)
print("First student's marks:", marks[0])

# Step 4: Change an element
marks[2] = 80  # Change 3rd student's marks to 80
print("Updated marks:", marks)

# Step 5: Add a new element
marks.append(95)
print("After adding new marks:", marks)

# Step 6: Loop through all elements
print("All marks:")
for mark in marks:
    print(mark)

# Step 7: Find average marks
average = sum(marks) / len(marks)
print("Average marks:", average)

# Step 8: Find maximum and minimum marks
max_marks = max(marks)
min_marks = min(marks)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)

# Step 9: Check if a mark exists
if 90 in marks:
    print("90 is in the marks list.")
else:
    print("90 is not in the marks list.")

# Step 10: Remove a mark
marks.remove(80)  # Remove the mark 80
print("After removing 80:", marks)

# Step 11: Clear the list
marks.clear()  # Clear all marks
print("Marks after clearing:", marks)

# Step 12: Create a new list with face encodings
# In a real-world application, you might be working with face encodings instead of marks.
# For example, if you're using a library like face_recognition, you would have a list
# of face encodings for different individuals.
face_encodings = [
    [0.1, 0.2, 0.3, 0.4],  # Encoding for person 1
    [0.2, 0.3, 0.4, 0.5],  # Encoding for person 2
    [0.3, 0.4, 0.5, 0.6],  # Encoding for person 3
]
# You can think of these encodings as unique identifiers for faces, similar to how marks identify
# students in a class. Each encoding is a list of numbers that represents the features of a face.
# You can access, update, and loop through these encodings just like you did with the marks list.
# For example, if you want to access the first face encoding:
print("First face encoding:", face_encodings[0])
# You can also update a face encoding:
face_encodings[1] = [0.5, 0.6, 0.7, 0.8]  # Update encoding for person 2
print("Updated face encodings:", face_encodings)
# You can loop through all face encodings:
print("All face encodings:")
for encoding in face_encodings:
    print(encoding)
# In this example, you can see how you can manage a list of face encodings in a similar way to how you managed the marks list.
# This is useful in applications like facial recognition systems, where you need to store and manipulate data about faces.
# In this example, you can think of the marks as data points for students in a class
# and the face encodings as data points for faces in a facial recognition system.
# In a facial recognition system, you would typically have a list of face encodings,
# where each encoding corresponds to a unique face.
# You can think of these encodings as unique identifiers for faces, similar to how marks identify
# students in a class. Each encoding is a list of numbers that represents the features of a face.
# You can access, update, and loop through these encodings just like you did with the marks list.
# For example, if you want to access the first face encoding:
print("First face encoding:", face_encodings[0])
# You can also update a face encoding:
face_encodings[1] = [0.5, 0.6, 0.7, 0.8]  # Update encoding for person 2
print("Updated face encodings:", face_encodings)
# You can loop through all face encodings:
print("All face encodings:")
for encoding in face_encodings:
    print(encoding)
# In this example, you can see how you can manage a list of face encodings in a similar way to how you managed the marks list.
# This is useful in applications like facial recognition systems, where you need to store and manipulate data about faces.
# In a facial recognition system, you would typically have a list of face encodings,
# where each encoding corresponds to a unique face.
# You can think of these encodings as unique identifiers for faces, similar to how marks identify
# students in a class. Each encoding is a list of numbers that represents the features of a face.
# You can access, update, and loop through these encodings just like you did with the marks list.
# For example, if you want to access the first face encoding:
print("First face encoding:", face_encodings[0])
# You can also update a face encoding:
face_encodings[1] = [0.5, 0.6, 0.7, 0.8]  # Update encoding for person 2
print("Updated face encodings:", face_encodings)
# You can loop through all face encodings:
print("All face encodings:")
for encoding in face_encodings:
    print(encoding)
# In this example, you can see how you can manage a list of face encodings in a similar way to how you managed the marks list.
# This is useful in applications like facial recognition systems, where you need to store and manipulate data about faces.
# In a facial recognition system, you would typically have a list of face encodings,
# where each encoding corresponds to a unique face.
# You can think of these encodings as unique identifiers for faces, similar to how marks identify
# students in a class. Each encoding is a list of numbers that represents the features of a face.
# You can access, update, and loop through these encodings just like you did with the marks list.
# For example, if you want to access the first face encoding:
print("First face encoding:", face_encodings[0])
# You can also update a face encoding:
face_encodings[1] = [0.5, 0.6, 0.7, 0.8]  # Update encoding for person 2
print("Updated face encodings:", face_encodings)
# You can loop through all face encodings:
print("All face encodings:")
for encoding in face_encodings:
    print(encoding)
# In this example, you can see how you can manage a list of face encodings in a similar way to how you managed the marks list.
# This is useful in applications like facial recognition systems, where you need to store and manipulate data about faces.
# In a facial recognition system,
# you would typically have a list of face encodings,
# where each encoding corresponds to a unique face.
# You can think of these encodings as unique identifiers for faces, similar to how marks identify
# students in a class. Each encoding is a list of numbers that represents the features of a face.
# You can access, update, and loop through these encodings just like you did with the marks list.
# For example, if you want to access the first face encoding:
print("First face encoding:", face_encodings[0])
# You can also update a face encoding:
face_encodings[1] = [0.5, 0.6, 0.7, 0.8]  # Update encoding for person 2
print("Updated face encodings:", face_encodings)
# You can loop through all face encodings:
print("All face encodings:")
for encoding in face_encodings:
    print(encoding) 

#Instead of marks, you’ll store face encodings (which are just big number arrays).

#You’ll access, update, and loop through them exactly like this.
print("\nData processing completed successfully.")