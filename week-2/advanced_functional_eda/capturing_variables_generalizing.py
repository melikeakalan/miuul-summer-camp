#############################################
# Değişkenlerin Yakalanması ve İşlemlerin Genelleştirilmesi
#############################################

# - kategorik değişken: category, bool ve  object tiplerinin hepsi        (cat_cols)
# - sinsirella değişken: tip bilgisi nümerik ama aslında kategorik olan   (num_but_cat)
# - cardinality'si yüksek değişken: ölçülemeyecek kadar fazla sınıfı olan (cat_but_car)


import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()
df.info()


# docstring
# hayat kurtaran fonksiyon
# Değişkenin eşsiz değer sayısı 10'dan küçükse kategorik, 20'den büyükse cardinal değişken kabul et
def grab_col_names(dataframe, cat_th=10, car_th=20):
    """
    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ----------
    dataframe: dataframe
            Değişken isimleri alınmak istenen dataframe'dir.
    cat_th: int, float
            numerik fakat kategorik olan değişkenler için sınıf eşik değeri
    car_th: int, float
            kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    -------
    cat_cols: list
            Kategorik değişken listesi
    num_cols: list
            Numerik değişken listesi
    cat_but_car: list
            Kategorik görünümlü kardinal değişken listesi

    Notes
    ------
    cat_cols + num_cols + cat_but_car = toplam değişken sayısı
    num_but_cat cat_cols'un içerisinde.

    """
    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if str(dataframe[col].dtypes) in ["category", "object", "bool"]]

    num_but_cat = [col for col in dataframe.columns if
                   dataframe[col].nunique() < 10 and dataframe[col].dtypes in ["int64", "float"]]

    cat_but_car = [col for col in dataframe.columns if
                   dataframe[col].nunique() > 20 and str(dataframe[col].dtypes) in ["category", "object"]]

    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes in ["int64", "float"]]
    num_cols = [col for col in num_cols if col not in cat_cols]

    print(f"Observations: {dataframe.shape[0]}")    # number of rows
    print(f"Variables: {dataframe.shape[1]}")       # number of columns
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')

    return cat_cols, num_cols, cat_but_car


cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist()
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in num_cols:
    num_summary(df, col, plot=True)


# BONUS
# bool tipli kategorik değişkenlerde countplot'un kullanılması

df = sns.load_dataset("titanic")
df.info()

for col in df.columns:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype('int64')

# bool tipli değişkenler, int tipine çevrildikten sonra grab_col_names func. ile atama işlemlerini tekrar yaparız
# çünkü cat_cols'ta olan bool tipli değişkenler artık num_but_cat'te olur ve bunları tekrar cat_cols'a ekleriz.
# ör. adult_male ve alone değişkenleri artık int64 tipli kategorik değişkenlerdir.
cat_cols, num_cols, cat_but_car = grab_col_names(df)
df.info()


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)


for col in num_cols:
    num_summary(df, col, plot=True)

