# Входные данные
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

# Определение результата соревнования
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Ничья!'

# Использование %
# Количество участников первой команды
team1_str = "В команде Мастера кода участников: %d !" % team1_num
print(team1_str)

# Количество участников в обеих командах
total_participants_str = "Итого сегодня в командах участников: %d и %d !" % (team1_num, team2_num)
print(total_participants_str)

# Использование format()
# Количество задач решённых командой 2
score_2_str = "Команда Волшебники данных решила задач: {} !".format(score_2)
print(score_2_str)

# Время за которое команда 2 решила задачи
team2_time_str = "Волшебники данных решили задачи за {:.1f} с !".format(team2_time)
print(team2_time_str)

# Использование f-строк
# Количество решённых задач по командам
scores_str = f"Команды решили {score_1} и {score_2} задач."
print(scores_str)

# Исход соревнования
challenge_result_str = f"Результат битвы: {challenge_result}"
print(challenge_result_str)

# Количество задач и среднее время решения
tasks_total_str = f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!"
print(tasks_total_str)
