fruits = ["apple", "banana", "orange"]
print("Fruits:")
for fruit in fruits:
    print("-", fruit)

student = {
    "name": "Siam",
    "age": 20,
    "city": "Dhaka",
}

print("\nStudent values:")
for value in student.values():
    print(value)

student["is_graduated"] = False
print("\nUpdated student dictionary:")
print(student)
