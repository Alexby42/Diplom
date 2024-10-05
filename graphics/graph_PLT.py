import matplotlib.pyplot as plt
import pandas as pd

# Загрузка данных из CSV файла
df = pd.read_csv('MSFT.csv', sep=',')  # df - data frame
df.head()  # Выбор всех данных

# Назначение переменных данным из CSV файла
a = df['year']  # Год
b = df['earnings']  # Выручка
c = df['revenue']  # Чистая прибыль
d = df['gross_profit']  # Валовая прибыль

# Создание линейного графика
plt.figure(figsize=(10, 8))  # Задание размера графика
plt.title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)  # Название графика
plt.xlabel('Год', color='gray')  # Название оси х
plt.ylabel('Млрд. $', color='gray')  # Название оси у
plt.plot(a, b, color='green', marker='^', markersize=6)  # Построение кривой
plt.plot(a, c, 'r--', linewidth=3, marker='o', markersize=6)  # Вариант построения кривой
plt.plot(a, d, color='blue', marker='*', markersize=7)  # Построение кривой
plt.legend(['Чистая прибыль', 'Выручка', 'Валовая прибыль'], loc=2, title='Условные обозначения:')  # Создание легенды
plt.grid()  # Отображение сетки
plt.savefig('linear_PLT.png')  # Сохранение графика в файл
plt.show()  # Вызов графика

# Создание столбчатой диаграммы
plt.figure(figsize=(10, 8))
plt.title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)
plt.xlabel('Год', color='gray')
plt.ylabel('Млрд. $', color='gray')
plt.bar(a, c, color='r')
plt.bar(a, d, color='b')
plt.bar(a, b, color='g')
plt.legend(['Выручка', 'Валовая прибыль', 'Чистая прибыль'], loc=2, title='Условные обозначения:')
plt.savefig('bar_PLT.png')
plt.show()

# Создание круговой диаграммы
plt.figure(figsize=(10, 10))
df[df.columns[1:4]].sum().plot.pie(autopct='%1.1f%%', labels=None, explode=[0.1, 0, 0])
plt.legend(['Чистая прибыль', 'Выручка', 'Валовая прибыль'], loc=2, title='Условные обозначения:')
plt.title('Общие финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)
plt.savefig('circular_PLT.png')
plt.show()
