marks = []
for i in range(1, 6):
    score = float(input(f"Enter marks for subject {i}: "))
    marks.append(score)

total = sum(marks)
percentage = total / 5

print(f"Total Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
