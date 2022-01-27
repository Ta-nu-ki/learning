import pandas as pd


def abc_analysis(data, metrics):
    """ Функция, выполняющая ABC-анализ на основе указанной метрики """
    try:
        data.sort_values(metrics, ascending=False, inplace=True)
        cum_sum = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY'])[metrics].cumsum()
        total_sum = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY'])[metrics].transform('sum')
        running_share = cum_sum / total_sum
        result = running_share.apply(classify_goods)
    except KeyError:
        print(f"Поля {metrics} нет в данных!")
        return
    return result


def classify_goods(share, class_a=0.85, class_b=0.1):
    """ Функция, маркирующая товары классами, в зависимости от указанных долей """
    if share <= class_a:
        return 'A'
    elif class_a < share <= (class_a + class_b):
        return 'B'
    else:
        return 'C'


# загружаем данные из файлов
data_sales = pd.read_csv(r"C:\Users\User\Downloads\sales.csv", header=0, sep=';')
data_products = pd.read_csv(r"C:\Users\User\Downloads\products.csv", header=0, sep=';')
# обходим ошибку в данных в названии поля PRODUCT
df = pd.merge(data_sales, data_products, how="left", left_on='PRODUCT', right_on='PRODUCT ')

# формируем поле ГОД
df["YEAR"] = pd.to_datetime(df["MONTH"], format="%Y%m").dt.year
# считаем выручку по каждому товару в рублях
df["SALES_RUB"] = df["PRICE"] * df["SALES_QNTY"]
# выкидываем ненужные поля
df.drop(["MONTH", 'PRODUCT ', 'PRICE'], axis=1, inplace=True)

# агрегируем данные в разрезе 'YEAR', 'STORE_FORMAT', 'CATEGORY'
df = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY', 'PRODUCT']).sum()

# проводим ABC-анализ по обороту в штуках
df['ABC_QNTY'] = abc_analysis(df, "SALES_QNTY")
# проводим ABC-анализ по обороту в рублях
df['ABC_RUB'] = abc_analysis(df, "SALES_RUB")
# итоговый результат
result = pd.DataFrame(df.to_records())[["YEAR", "STORE_FORMAT", "CATEGORY", "PRODUCT", "ABC_QNTY", "ABC_RUB"]]
result.sort_values(["YEAR", "STORE_FORMAT", "CATEGORY", "PRODUCT"], inplace=True)