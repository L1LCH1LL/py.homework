# Загрузка df
# вариант 1
adv2_df = pd.read_csv('advertising_2.csv', index_col='Number')
# вариант 2
adv2_df = pd.read_csv('advertising_2.csv')
adv2_df = adv2_df.set_index('Number')
# вариант 3
adv2_df = pd.read_csv('advertising_2.csv')
adv2_df.set_index('Number', inplace=True)
# Отображение пользователей с номерами с 533 по 536
# вариант 1
adv2_df.loc[533:536]
# вариант 2 (приоритет)
adv2_df.loc[533:536, :]
# вариант 3
adv2_df.iloc[3:7]