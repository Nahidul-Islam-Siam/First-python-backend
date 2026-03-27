name = input("Student name: ")
mark1 = int(input("Subject 1 mark: "))
mark2 = int(input("Subject 2 mark: "))
mark3 = int(input("Subject 3 mark: "))

total = mark1 + mark2 + mark3
average = total / 3

if average >= 80:
    grade = "A"
elif average >= 60:
    grade = "B"
elif average >= 40:
    grade = "C"
else:
    grade = "F"

print("\nResult Summary")
print("Name:", name)
print("Total:", total)
print("Average:", round(average, 2))
print("Grade:", grade)
