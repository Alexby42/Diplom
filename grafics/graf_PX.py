import plotly.express as px
import pandas as pd
import plotly.graph_objs as go

# Загрузка данных из CSV файла
df = pd.read_csv('MSFT.csv', sep=',')  # df - data frame
# Выбор всех данных
df.head()

# Назначение переменных данным из CSV файла
a = df['year']  # Год
b = df['earnings']  # Выручка
c = df['revenue']  # Чистая прибыль
d = df['gross_profit']  # Валовая прибыль

# Создание линейного графика
fig = go.Figure()  # Создание графика
fig.add_trace(go.Scatter(x=a, y=b, mode='lines+markers', name='Чистая прибыль'))  # Добавление на график кривой
fig.add_trace(go.Scatter(x=a, y=c, mode='lines+markers', name='Выручка'))
fig.add_trace(go.Scatter(x=a, y=d, mode='lines+markers', name='Валовая прибыль', line=dict(color='green', width=5,
                                                                                           dash='dot')))
fig.update_layout(title='Финансовые показатели Microsoft Corporation с 2011-2024гг.')  # Название графика
fig.update_layout(yaxis_title='Млрд. $', xaxis_title='Год', title={'font': dict(size=50), 'x': 0.5},
                  legend_orientation='h', legend_font_size=25)  # Название осей и доп. параметры
fig.update_xaxes(gridcolor='black', minor_griddash='dot', titlefont=dict(size=22), tickfont=dict(size=19))  # Параметры оси х
fig.update_yaxes(titlefont=dict(size=22), tickfont=dict(size=19))  # Параметры оси y
fig.update_traces(hoverinfo='all', hovertemplate='Год: %{x}<br>Объем: %{y}')  # Оформление всплывающей подсказки
fig.write_image('linear_PX.png')  # Сохранение графика в файл
fig.show()  # Вызов графика

# Создание столбчатой диаграммы
fig = go.Figure(data=[
    go.Bar(x=a, y=c, name='Выручка'),
    go.Bar(x=a, y=d, name='Валовая прибыль'),
    go.Bar(x=a, y=b, name='Чистая прибыль'),
])
fig.update_layout(barmode='overlay', title='Финансовые показатели Microsoft Corporation с 2011-2024гг.')
fig.update_layout(yaxis_title='Млрд. $', xaxis_title='Год', title={'font': dict(size=50), 'x': 0.5},
                  legend_orientation='h', legend_font_size=25)
fig.update_xaxes(titlefont=dict(size=22), tickfont=dict(size=19))
fig.update_yaxes(titlefont=dict(size=22), tickfont=dict(size=19))
fig.update_traces(hoverinfo='all', hovertemplate='Год: %{x}<br>Объем: %{y}')
fig.write_image('bar_PX.png')
fig.show()

# Создание круговой диаграммы
data = [df['earnings'].sum(), df['revenue'].sum(), df['gross_profit'].sum()]
labels = ['Чистая прибыль', 'Выручка', 'Валовая прибыль']
fig = px.pie(df, values=data, names=labels, title='Общие финансовые показатели Microsoft Corporation с 2011-2024гг.')
fig.update_layout(title={'font': dict(size=25), 'x': 0.5}, legend_title='Условные обозначения:',
                  legend=dict(font=dict(size=20)), font={'size': 22})
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.write_image('circular_PX.png')
fig.show()
