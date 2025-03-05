import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Загрузка данных
df = pd.read_csv('data.csv')
# Проверка названий столбцов
print(df.columns)
sns.lineplot(x='age', y='spending_score', data=df)
plt.title('Age vs Spending Score')
plt.xlabel('Age')
plt.ylabel('Spending Score')
plt.show()