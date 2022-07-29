#############################################
# 3. Encoding (Label Encoding, One-Hot Encoding, Rare Encoding)
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)


def load_application_train():
    data = pd.read_csv("week-3/datasets/application_train.csv")
    return data


def load():
    data = pd.read_csv("week-3/datasets/titanic.csv")
    return data


df = load()


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Veri setindeki kategorik, numerik ve kategorik fakat kardinal değişkenlerin isimlerini verir.
    Not: Kategorik değişkenlerin içerisine numerik görünümlü kategorik değişkenler de dahildir.

    Parameters
    ------
        dataframe: dataframe
                Değişken isimleri alınmak istenilen dataframe
        cat_th: int, optional
                numerik fakat kategorik olan değişkenler için sınıf eşik değeri
        car_th: int, optinal
                kategorik fakat kardinal değişkenler için sınıf eşik değeri

    Returns
    ------
        cat_cols: list
                Kategorik değişken listesi
        num_cols: list
                Numerik değişken listesi
        cat_but_car: list
                Kategorik görünümlü kardinal değişken listesi

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        cat_cols + num_cols + cat_but_car = toplam değişken sayısı
        num_but_cat cat_cols'un içerisinde.
        Return olan 3 liste toplamı toplam değişken sayısına eşittir: cat_cols + num_cols + cat_but_car = değişken sayısı

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car


#############################################
# Label Encoding & Binary Encoding
#############################################

"""
# Binary Encoding de bir label encoding'tir.
# Eğer dönüştürülecek değişkenin iki sınıfı varsa 0 ve 1 ile temsil edilir.
# Eğer dönüştürülecek değişken ikiden fazla sınıfı var ve ordinalse 0, 1, 2, ... şek temsil edilir.
# LabelEncoder: alfabetik sıraya göre ilk gördüğü değere sıfır verir. ör. female: 0, male: 1"""

le = LabelEncoder()
le.fit_transform(df["Sex"])[0:5]

# 0, 1 sınıfları hangi değişkenleri temsil ediyor?
le.inverse_transform([0, 1])


def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe


df = load()
df.info()  # numeric types

"""
Dikkat!
Burada df[col] un toplam unique değer sayısını nunique() ile almamızın nedeni,
eğer len(df[col].unique()) seçili değişkendeki NaN değerleri de bir unique olarak alırdı.
Fakat nunique, eksik değerleri almaz."""
binary_cols = [col for col in df.columns if df[col].dtype not in ['int64', float]
               and df[col].nunique() == 2]

for col in binary_cols:
    label_encoder(df, col)

df.head()

df = load_application_train()
df.shape
df.dtypes

binary_cols = [col for col in df.columns if df[col].dtype not in ['int64', float]
               and df[col].nunique() == 2]

df[binary_cols].head()

"""
# Dikkat!
# Tüm binary sütunlara label encoding yaptıktan sonra NaN olan hücereler 2 olmuş.
# label_encoder: eksik değerlere de değer atar"""
for col in binary_cols:
    label_encoder(df, col)

df[binary_cols].head()

df = load()
df["Embarked"].value_counts()
df["Embarked"].nunique()
len(df["Embarked"].unique())

#############################################
# One-Hot Encoding
#############################################

df = load()
df.head()
df["Embarked"].value_counts()

pd.get_dummies(df, columns=["Embarked"]).head()

# dummy değişken tuzağı!! alfabeye göre oluşturulan ilk column drop edilir
pd.get_dummies(df, columns=["Embarked"], drop_first=True).head()

# ilgili değişkendeki eksik değerler de bir değişken olarak gelsin
pd.get_dummies(df, columns=["Embarked"], dummy_na=True).head()

# binary encoding & one-hot encoding
pd.get_dummies(df, columns=["Sex", "Embarked"], drop_first=True).head()


def one_hot_encoder(dataframe, categorical_cols, drop_first=True):
    dataframe = pd.get_dummies(dataframe, columns=categorical_cols, drop_first=drop_first)
    return dataframe


df = load()

# cat_cols, num_cols, cat_but_car = grab_col_names(df)

ohe_cols = [col for col in df.columns if 10 >= df[col].nunique() > 2]

one_hot_encoder(df, ohe_cols).head()

df.head()

#############################################
# Rare Encoding
#############################################

# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
# 3. Rare encoder yazacağız.

###################
# 1. Kategorik değişkenlerin azlık çokluk durumunun analiz edilmesi.
###################

df = load_application_train()
df["NAME_EDUCATION_TYPE"].value_counts()

cat_cols, num_cols, cat_but_car = grab_col_names(df)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show()


for col in cat_cols:
    cat_summary(df, col)

"""
XNA sınıfı silinmelidir. Bütün veride 0.001 oranında görülmüş.
Bu sınıf değişkene dönüştürüldüğünde, bir tahmin probleminde bu değişkenin kullanılmaması için."""
#      CODE_GENDER  Ratio
# F         202448 65.834
# M         105059 34.164
# XNA            4  0.001

""" Unemployed, Student, Businessman, Maternity sınıfları birleştirilerek rare encoder yapılarak birleştirilmeli.
Fakat bu sınıfların target ortalamaları da birbirine yakın olmalıdır. """
#                       NAME_INCOME_TYPE  Ratio
# Working                         158774 51.632
# Commercial associate             71617 23.289
# Pensioner                        55362 18.003
# State servant                    21703  7.058
# Unemployed                          22  0.007
# Student                             18  0.006
# Businessman                         10  0.003
# Maternity leave                      5  0.002


###################
# 2. Rare kategoriler ile bağımlı değişken arasındaki ilişkinin analiz edilmesi.
###################

df["NAME_INCOME_TYPE"].value_counts()

df.groupby("NAME_INCOME_TYPE")["TARGET"].mean()


def rare_analyser(dataframe, target, cat_cols):
    """
    Hayat kurtaran func.
    Bol kategorik değişkenli veri setinde bunu kullanmalıyız.
    """

    for col in cat_cols:
        print(col, ":", len(dataframe[col].value_counts()))
        print(pd.DataFrame({"COUNT": dataframe[col].value_counts(),
                            "RATIO": dataframe[col].value_counts() / len(dataframe),
                            "TARGET_MEAN": dataframe.groupby(col)[target].mean()}), end="\n\n\n")


rare_analyser(df, "TARGET", cat_cols)


#############################################
# 3. Rare encoder'ın yazılması.
#############################################

def rare_encoder(dataframe, rare_perc):
    """
    Veri setindeki seyrek sınıflı kategorik değişkenlerin seyrek sınıflarını toplayıp, birleştirir.

    Fonksiyona girilen rare oranından daha düşük sayıda bu kategorik değişkenin,
    sınıf oranı varsa bu sınıfları rare columns olarak getir.

    tmp: veri setindeki rare_columns'un oranı
    len(temp_df): toplam gözlem sayısı
    np.where(): ilgili değişkenin içerisinde rare labelları görürürsen, rare olarak gördüğün yerlere 'Rare' yaz
                Eğer ilgili değişken rare_labels içerisinde değilse olduğu gibi bırak.
    """
    temp_df = dataframe.copy()

    rare_columns = [col for col in temp_df.columns if temp_df[col].dtypes == 'O'
                    and (temp_df[col].value_counts() / len(temp_df) < rare_perc).any(axis=None)]

    for var in rare_columns:
        tmp = temp_df[var].value_counts() / len(temp_df)
        rare_labels = tmp[tmp < rare_perc].index
        temp_df[var] = np.where(temp_df[var].isin(rare_labels), 'Rare', temp_df[var])

    return temp_df


new_df = rare_encoder(df, 0.01)

rare_analyser(new_df, "TARGET", cat_cols)

# çok fazla sınıflı değişken
df["OCCUPATION_TYPE"].value_counts()


#############################################
# Feature Scaling (Özellik Ölçeklendirme)
#############################################

###################
# StandardScaler:
###################
# Klasik standartlaştırma, Normalleştirme, z standartlaştırılması da denir.
# Ortalama, bütün gözlem birimlerinden çıkarılır ve standart sapmaya bölünür. z = (x - u) / s

df = load()
ss = StandardScaler()
df["Age_standard_scaler"] = ss.fit_transform(df[["Age"]])
df.head()

###################
# RobustScaler:
###################
# Dikkat!
# Standart sapma ve ortalama veri setindeki aykırı değerlerden etkilenen metriklerdir.
# Bütün gözlem birimlerinden medyanı çıkar ve iqr'a böl.

rs = RobustScaler()
df["Age_robuts_scaler"] = rs.fit_transform(df[["Age"]])
df.describe().T

###################
# MinMaxScaler:
###################
# Verilen 2 değer arasında değişken dönüşümü yapar. (default 0-1 aralığı)
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))
# X_scaled = X_std * (max - min) + min

mms = MinMaxScaler()
df["Age_min_max_scaler"] = mms.fit_transform(df[["Age"]])
df.describe().T

df.head()

age_cols = [col for col in df.columns if "Age" in col]


def num_summary(dataframe, numerical_col, plot=False):
    quantiles = [0.05, 0.10, 0.20, 0.30, 0.40, 0.50, 0.60, 0.70, 0.80, 0.90, 0.95, 0.99]
    print(dataframe[numerical_col].describe(quantiles).T)

    if plot:
        dataframe[numerical_col].hist(bins=20)
        plt.xlabel(numerical_col)
        plt.title(numerical_col)
        plt.show(block=True)


for col in age_cols:
    num_summary(df, col, plot=True)

###################
# Numeric to Categorical: Sayısal Değişkenleri Kateorik Değişkenlere Çevirme
# Binning
###################

# Age değişkenini beş parça o.ş. böl
# Dönüştürülecek değişkenin, dönüştürüleceği sınıflar belliyse label argümanını kullan
# qcut: değişkenin değerlerini küçükten büyüğe sıralar, çeyrek değerlere göre beş parçaya böler
df["Age_qcut"] = pd.qcut(df['Age'], 5)

df.head()

