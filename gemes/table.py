#Пример строки с выводом таблицы умножения
# 1 * 1 = 1
# 1 * 2 = 2

count = 0
print("Рисуем таблицу умножения")

for i in range(1, 11):
    for j in range(1, 11):
        count = i * j
        print(f'{i} * {j} = {count}')


