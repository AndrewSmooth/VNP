import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Настройка стиля графиков
plt.style.use('seaborn-v0_8')
plt.rcParams['figure.figsize'] = (10, 6)
plt.rcParams['font.size'] = 12

print("✅ Библиотеки загружены.")

# === Задание №1 ===
print("=== Задание №1: Экспоненциальный поток (λ = 0.1 /сек) ===")

lam = 0.1  # интенсивность, 1/сек
N1 = 100

# Генерация интервалов между заявками
inter_arrival_times = np.random.exponential(1/lam, size=N1)
arrival_times = np.cumsum(inter_arrival_times)

# Расчёт средних
emp_mean_time = np.mean(inter_arrival_times)
theo_mean_time = 1 / lam

print(f"Эмпирическое среднее время между заявками: {emp_mean_time:.3f} с")
print(f"Теоретическое среднее: {theo_mean_time:.3f} с")

# График функции обратного преобразования
P = np.linspace(0.001, 0.999, 500)
t_theory = -np.log(1 - P) / lam

plt.figure(figsize=(8, 5))
plt.plot(P, t_theory, 'b-', linewidth=2, label=r'$t = -\frac{\ln(1-P)}{\lambda}$')
plt.xlabel('Вероятность P')
plt.ylabel('Время t (с)')
plt.title('Функция обратного преобразования для экспоненциального закона')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# Гистограмма + теоретическая плотность
plt.figure(figsize=(8, 5))
count, bins, _ = plt.hist(inter_arrival_times, bins=30, density=True,
                           alpha=0.6, color='skyblue', edgecolor='black',
                           label='Эмпирическое')

x = np.linspace(0, max(bins), 200)
y = lam * np.exp(-lam * x)
plt.plot(x, y, 'r-', lw=2, label=f'Теория: λ={lam}')
plt.xlabel('Время между заявками (с)')
plt.ylabel('Плотность вероятности')
plt.title('Распределение интервалов между заявками')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()