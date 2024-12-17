data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
total_sum = 0
count = 0
for sublist in data:
    for number in sublist:
        total_sum += number
        count += 1
average = total_sum / count
print(f"Середнє арифметичне {average}")
