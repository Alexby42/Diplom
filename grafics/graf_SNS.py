import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
df = pd.read_csv('MSFT.csv', sep=',')
df.head()

# Назначение переменных данным из CSV файла
a = df['year']
b = df['earnings']
c = df['revenue']
d = df['gross_profit']

# Создание линейного графика
plt.figure(figsize=(10, 8))
sns.set_style('darkgrid') # Заливка фона графика
sb = sns.lineplot(data=df, x=a, y=b, color='green', marker='^', markersize=7, label='Чистая прибыль')
sb1 = sns.lineplot(data=df, x=a, y=c, color='blue', marker='d', markersize=7, label='Выручка')
sb2 = sns.lineplot(data=df, x=a, y=d, color='red', marker='h', markersize=7, label='Валовая прибыль')
plt.xlabel('Год', color='gray')
plt.ylabel('Млрд. $', color='gray')
plt.legend(title='Условные обозначения:')
sb.set_title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)
plt.savefig('linear_SNS.png')
plt.show()

#Создание столбчатой диаграммы
plt.figure(figsize=(14, 8))
sns.set(context='notebook', style='darkgrid', palette='deep')  #Установка стиля графика
sbn = sns.barplot(x=a, y=b, data=df, color='blue', label='Чистая прибыль')
sbn1 = sns.barplot(x=a, y=c, data=df, color='red', label='Выручка')
sbn2 = sns.barplot(x=a, y=d, data=df, color='green', label='Валовая прибыль')
plt.legend(title='Условные обозначения:')
sbn.set(xlabel='Год', ylabel='Млрд. $', title='Финансовые показатели Microsoft Corporation с 2011-2024гг.')
plt.savefig('bar_SNS.png')
plt.show()

# Создание круговой диаграммы
plt.figure(figsize=(10, 9))
colors = sns.color_palette('deep')[0:3]
df[df.columns[1:4]].sum().plot.pie(autopct='%1.1f%%', labels=None, colors=colors)
plt.legend(['Чистая прибыль', 'Выручка', 'Валовая прибыль'], title='Условные обозначения:', loc=2)
plt.title('Финансовые показатели Microsoft Corporation с 2011-2024гг.', fontsize=16)
plt.savefig('circular_SNS.png')
plt.show()
