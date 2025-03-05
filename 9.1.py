# Загрузка df
# вариант 1
adv1_df = pd.read_csv('advertising_1.csv', index_col='Number')
# вариант 2
adv1_df = pd.read_csv('advertising_1.csv')
adv1_df = adv1_df.set_index('Number')
# вариант 3
adv1_df = pd.read_csv('advertising_1.csv')
adv1_df.set_index('Number', inplace=True)
# Отображение первых 10 строк
# вариант 1 (приоритет)
adv1_df.head(10)
# вариант 2 (приоритет)
adv1_df[:10]
# вариант 3
adv1_df.loc[:10 , :]