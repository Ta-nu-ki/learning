import pandas as pd


def abc_analysis(data, metrics):
    """ 
    Performs ABC-analysis based on the specified metric. The metric must be contained in the data.
    """
    try:
        data.sort_values(metrics, ascending=False, inplace=True)
        cum_sum = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY'])[metrics].cumsum()
        total_sum = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY'])[metrics].transform('sum')
        running_share = cum_sum / total_sum
        result = running_share.apply(classify_goods)
    except KeyError:
        print(f"There is no {metrics} field in the data!")
        return
    return result


def classify_goods(share, class_a=0.85, class_b=0.1):
    """ 
    Marks a product with the corresponding class.
    """
    if share <= class_a:
        return 'A'
    elif class_a < share <= (class_a + class_b):
        return 'B'
    else:
        return 'C'


# Loads data from files.
data_sales = pd.read_csv(r"sales.csv", header=0, sep=';')
data_products = pd.read_csv(r"products.csv", header=0, sep=';')
# Misprint bypass in the name of the PRODUCT field. 
df = pd.merge(data_sales, data_products, how="left", left_on='PRODUCT', right_on='PRODUCT ')

# Formats the YEAR field as YYYY.
df["YEAR"] = pd.to_datetime(df["MONTH"], format="%Y%m").dt.year
# Calculates the revenue of each product in rubles.
df["SALES_RUB"] = df["PRICE"] * df["SALES_QNTY"]
# Drops uneeded columns.
df.drop(["MONTH", 'PRODUCT ', 'PRICE'], axis=1, inplace=True)

# Aggregates data.
df = df.groupby(['YEAR', 'STORE_FORMAT', 'CATEGORY', 'PRODUCT']).sum()

# Performs ABC-analysis.
df['ABC_QNTY'] = abc_analysis(df, "SALES_QNTY")
df['ABC_RUB'] = abc_analysis(df, "SALES_RUB")

result = pd.DataFrame(df.to_records())[["YEAR", "STORE_FORMAT", "CATEGORY", "PRODUCT", "ABC_QNTY", "ABC_RUB"]]
result.sort_values(["YEAR", "STORE_FORMAT", "CATEGORY", "PRODUCT"], inplace=True)