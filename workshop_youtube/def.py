number_1 = [1, 2, 3, 4, 5]
number_2 = [6, 7, 8, 9, 10]


def find_average(numbers):
    avgerage = sum(numbers) / len(numbers)
    return avgerage


average_1 = find_average(number_1)
average_2 = find_average(number_2)
print(average_1, average_2)