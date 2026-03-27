number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

print("\nFor loop: 1 to 5")
for i in range(1, 6):
    print(i)

print("\nWhile loop: 5 to 1")
count = 5
while count >= 1:
    print(count)
    count -= 1
