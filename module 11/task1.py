import requests

# Отправляем GET-запрос к сайту
response = requests.get('https://api.github.com')

# Проверяем статус ответа
if response.status_code == 200:
    # Выводим содержимое ответа в консоль
    print(response.json())
else:
    print(f"Ошибка: {response.status_code}")

#########################################################################

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

def lorenz_system(t, xyz, sigma=10, rho=28, beta=8/3):
    x, y, z = xyz
    dxdt = sigma * (y - x)
    dydt = x * (rho - z) - y
    dzdt = x * y - beta * z
    return [dxdt, dydt, dzdt]

# Начальные условия
xyz0 = [1.0, 1.0, 1.0]




# Временной интервал
t_span = (0, 50)
t_eval = np.linspace(*t_span, 10000)

# Решаем систему Лоренца
solution = solve_ivp(lorenz_system, t_span, xyz0, t_eval=t_eval)


# Визуализация результатов
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution.y[0], solution.y[1], solution.y[2])



ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

plt.show()
