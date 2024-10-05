import seaborn as sns
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
sns.set_style('darkgrid')  # Заливка фона графика
sb = sns.lineplot(x=a, y=b, color='green', marker='^', markersize=7, label='Чистая прибыль')  # Построение кривой
sb1 = sns.lineplot(x=a, y=c, color='blue', marker='d', markersize=7, label='Выручка')
sb2 = sns.lineplot(x=a, y=d, color='red', marker='h', markersize=7, label='Валовая прибыль')
sb.set_title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)  # Название графика
plt.xlabel('Год', color='gray')  # Название оси х
plt.ylabel('Млрд. $', color='gray')  # Название оси y
plt.legend(title='Условные обозначения:')  # Название легенды
plt.savefig('linear_SNS.png')  # Сохранение графика в файл
plt.show()  # Вызов графика

#Создание столбчатой диаграммы
plt.figure(figsize=(14, 8))
sns.set(style='ticks', context='paper', font_scale=1.5)  # Установка стиля графика
sbn = sns.barplot(x=a, y=c, data=df, color='red', label='Выручка')
sbn1 = sns.barplot(x=a, y=d, data=df, color='green', label='Валовая прибыль')
sbn2 = sns.barplot(x=a, y=b, data=df, color='blue', label='Чистая прибыль')
sbn.set_title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=20)
sbn.set_xlabel('Год', fontsize=14)
sbn.set_ylabel('Млрд. $', fontsize=14)
plt.legend(title='Условные обозначения:')
plt.savefig('bar_SNS.png')
plt.show()

# Создание круговой диаграммы
plt.figure(figsize=(10, 10))
colors = sns.color_palette('deep')[0:3]  # Определение данных для параметра цвета
df[df.columns[1:4]].sum().plot.pie(autopct='%1.1f%%', labels=None, colors=colors, explode=[0.2, 0.1, 0], shadow=True)
plt.legend(['Чистая прибыль', 'Выручка', 'Валовая прибыль'], title='Условные обозначения:', loc=2)
plt.title('Общие финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)
plt.savefig('circular_SNS.png')
plt.show()
