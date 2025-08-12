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
    
# Step 9: Remove an element
marks.remove(80)  # Remove the mark of 3rd student
#Why this matters for Face Recognition later:

#Instead of marks, you’ll store face encodings (which are just big number arrays).

#You’ll access, update, and loop through them exactly like this.
