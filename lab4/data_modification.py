import pandas as pd


# Загрузка датасета
df = pd.read_csv('datasets/data.csv')

# Заполнение пропущенных значений в поле "Age" средним значением
mean_age = df['Age'].mean()

# Модификация датасета
df['Age'].fillna(mean_age, inplace=True)

# Сохранение модифицированного датасета
df.to_csv('datasets/modified_data.csv', index=False)
