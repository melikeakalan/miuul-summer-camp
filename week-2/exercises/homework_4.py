######################################################
# Fonksiyonlara Özellik ve Docstring Ekleme
# ####################################################

# GOREV-1: cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argümanla biçimlendirilebilir olsun. Var olan
# özelliği de argümanla kontrol edilebilir hale getirebilirsiniz.
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head(10)

cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)


# GOREV-2: check_df(), cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring
# yazınız. (task, params, return, example)
def cat_summary(dataframe, col_name, plot=False):
    """

    Parameters
    ----------
    dataframe: DataFrame
        değişken isimleri alınmak istenen dataframe'dir.
    col_name: cat_cols
        kategorik değişkenlerden herhangi biri
    plot: False
        döndürülen func. çizilsin mi?

    Returns
    -------
    df: DataFrame
      içerisinden kategorik değişken seçilecek veri seti
    col_name: str
       kategorik değişkenin ismi
    plot: bool
       Kategorik değişkenin veri setindeki dağılım oranını görmek için True olarak ayarlayın.

    Examples
    -------
    cat_summary(df, "sex", plot=True)

    """


def check_df(dataframe, head=5):
    """

    Parameters
    ----------
    dataframe: DataFrame
       özet bilgileri oluşturulacak df
    head: int
      dataframe'in ilk kaç gözlemi alınacağı

    Returns
    -------
    df: dataframe

    Examples
    -------
    check_df(df)

    Notes
    -------
    tek satırlık kod ile farklı veri setlerini özetleyen fonksiyon

    """
    print("##################### Shape #####################")
    print(dataframe.shape)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

