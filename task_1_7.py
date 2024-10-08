grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

list_students = sorted(students)

arithmetic_mean_dict = {}

for i in range(len(students)):
    arithmetic_mean_dict[list_students[i]] = round(sum(grades[i])/len(grades[i]), 2)

print( 'Словарь "Имя : средний балл":', arithmetic_mean_dict)