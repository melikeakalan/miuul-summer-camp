#############################################
# PANDAS
#############################################

# Pandas Series
# Veri Okuma (Reading Data)
# Veriye Hızlı Bakış (Quick Look at Data)
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
# Apply ve Lambda
# Birleştirme (Join) İşlemleri

#############################################
# Pandas Series
#############################################
import pandas as pd

s = pd.Series([10, 77, 12, 4, 5])
# 0    10
# 1    77
# 2    12
# 3     4
# 4     5

type(s)         # pandas.core.series.Series
s.index         # RangeIndex(start=0, stop=5, step=1)
s.dtype         # dtype('int64')
s.size          # 5
s.ndim          # 1
s.values        # array([10, 77, 12,  4,  5], dtype=int64)
type(s.values)  # numpy.ndarray

s.head(3)
# 0    10
# 1    77
# 2    12

s.tail(3)
# 2    12
# 3     4
# 4     5

#############################################
# Veri Okuma (Reading Data)
#############################################
import pandas as pd

df = pd.read_csv("week-2/datasets/advertising.csv")
df.head()
# different read_method with pandas documentation
# or pandas cheatsheet

#############################################
# Veriye Hızlı Bakış (Quick Look at Data)
#############################################
import pandas as pd
import seaborn as sns

# titanic: yolculuk esnasında meydana gelen kaza sonrasında
# yolcuların hayatta kalıp/kalmama durumlarını ifade eden veriseti
# survived: bağımlı değişken, hedef değişkendir. 1:yolcu hayatta kalmış, 0:yolcu hayatta kalamamış
df = sns.load_dataset("titanic")

df.head()   # shows first five rows of dataframe
#    survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0         0       3    male  22.0  ...   NaN  Southampton     no  False
# 1         1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2         1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3         1       1  female  35.0  ...     C  Southampton    yes  False
# 4         0       3    male  35.0  ...   NaN  Southampton     no   True

df.tail()  # shows last five rows of dataframe

df.shape   # (row, column) numbers

df.info()
# #   Column       Non-Null Count  Dtype
# ---  ------       --------------  -----
#  0   survived     891 non-null    int64
#  1   pclass       891 non-null    int64
#  2   sex          891 non-null    object
#  3   age          714 non-null    float64
#  4   sibsp        891 non-null    int64
#  5   parch        891 non-null    int64
#  6   fare         891 non-null    float64
#  7   embarked     889 non-null    object
#  8   class        891 non-null    category
#  9   who          891 non-null    object
#  10  adult_male   891 non-null    bool
#  11  deck         203 non-null    category
#  12  embark_town  889 non-null    object
#  13  alive        891 non-null    object
#  14  alone        891 non-null    bool
# dtypes: bool(2), category(2), float64(2), int64(4), object(5)

df.columns
df.index           # RangeIndex(start=0, stop=891, step=1)  last index: 890

df.describe().T
#             count       mean        std   min      25%      50%   75%       max
#   survived  891.0   0.383838   0.486592  0.00   0.0000   0.0000   1.0    1.0000
#   pclass    891.0   2.308642   0.836071  1.00   2.0000   3.0000   3.0    3.0000
#   age       714.0  29.699118  14.526497  0.42  20.1250  28.0000  38.0   80.0000
#   sibsp     891.0   0.523008   1.102743  0.00   0.0000   0.0000   1.0    8.0000
#   parch     891.0   0.381594   0.806057  0.00   0.0000   0.0000   0.0    6.0000
#   fare      891.0  32.204208  49.693429  0.00   7.9104  14.4542  31.0  512.3292

df.isnull().values.any()  # Veri setinde eksik değer varsa True döner
df.isnull().sum()         # Her bir değişkendeki(sütunda) eksik değer sayısını verir
df["sex"].head()

df["sex"].value_counts()  # değişkendeki değerleri gruplayıp kaçar tane olduğunu verir
# male      577
# female    314


#############################################
# Pandas'ta Seçim İşlemleri (Selection in Pandas)
#############################################
import pandas as pd
import seaborn as sns
df = sns.load_dataset("titanic")
df.head()

df.index

df[0:13]  # 0. satırdan 13. satıra kadar df'yi göster
#     survived  pclass     sex   age  ...  deck  embark_town  alive  alone
# 0          0       3    male  22.0  ...   NaN  Southampton     no  False
# 1          1       1  female  38.0  ...     C    Cherbourg    yes  False
# 2          1       3  female  26.0  ...   NaN  Southampton    yes   True
# 3          1       1  female  35.0  ...     C  Southampton    yes  False
# 4          0       3    male  35.0  ...   NaN  Southampton     no   True
# 5          0       3    male   NaN  ...   NaN   Queenstown     no   True
# 6          0       1    male  54.0  ...     E  Southampton     no   True
# 7          0       3    male   2.0  ...   NaN  Southampton     no  False
# 8          1       3  female  27.0  ...   NaN  Southampton    yes  False
# 9          1       2  female  14.0  ...   NaN    Cherbourg    yes  False
# 10         1       3  female   4.0  ...     G  Southampton    yes  False
# 11         1       1  female  58.0  ...     C  Southampton    yes   True
# 12         0       3    male  20.0  ...   NaN  Southampton     no   True
# [13 rows x 15 columns]

df.drop(0, axis=0).head()           # 0. satırı sil
df.drop("survived", axis=1).head()  # "survived" sütununu sil

# seçili indexlere göre satıları siler
delete_indexes = [1, 3, 5, 7]
df.drop(delete_indexes, axis=0).head(10)

# df = df.drop(delete_indexes, axis=0)

# DIKKAT! inplace argümanı yapılan değişikliğin kalıcı olmasını sağlar.
# df.drop(delete_indexes, axis=0, inplace=True)

#######################
# Değişkeni Indexe Çevirmek
#######################

df["age"].head()  # variable selection
df.age.head()     # variable selection

df.index = df["age"]

df.drop("age", axis=1).head()

df.drop("age", axis=1, inplace=True)
df.head()

#######################
# Indexi Değişkene Çevirmek
#######################

df.index

# 1. yol
df["age"] = df.index
df.head()

df.drop("age", axis=1, inplace=True)

# 2. yol
df.reset_index().head()
df = df.reset_index()
df.head()

#######################
# Değişkenler(sütunlar) Üzerinde İşlemler
#######################
import pandas as pd
import seaborn as sns

# df'deki tüm columnları görüntülemek için,
# gösterilecek olan max. column sayısı olmasın yani hepsini göster.
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

"age" in df   # değişken df'de var mı ?

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())    # pandas.core.series.Series

# DIKKAT! Tek bir değişken seçerken seçimin sonucunun df olarak kalması için [[]] kullanılmalı
df[["age"]].head()
type(df[["age"]].head())  # pandas.core.frame.DataFrame

# df'de birden çok değişken seçme
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

# df'ye yeni bir değişken ekleme
df["age2"] = df["age"]**2
df["age3"] = df["age"] / df["age2"]

# df'den değişken silme
df.drop("age3", axis=1).head()

# df'de birden çok değişken silme
df.drop(col_names, axis=1).head()

# df'de belirli string ifadeyi barındıran değişkenleri silme
# bütün satırları seç, df'nin columnlarına string operation yapılacak ve contains method kullanılacak
# ~: column isimleri içerisinde "age"'i barındırmayan columnları getir.
df.loc[:, ~df.columns.str.contains("age")].head()


#######################
# iloc & loc
#######################
# dataframe'lerde seçim için kullanılan özel yapılardır.

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# iloc: integer based selection, index bilgisiyle seçim yapar
df.iloc[0:3]        # df'i 0. satırdan 3. satıra kadar getir
df.iloc[0, 0]       # df'nin 0. satır 0. sütundaki elemanını getir

# loc: label based selection, indexlerdeki label'lara göre seçim yapar
df.loc[0:3]         # df'yi 0. satırdan 3. satır dahil getirir

df.iloc[0:3, 0:3]   # df'yi 0. satırdan 3. satıra kadar, 0. sütundan 3. sütuna kadar getirir
df.loc[0:3, "age"]  # df'yi 0. satırdan 3. satır dahil, age sütunuyla getir

# DIKKAT! loc'u fancy index ile kullanmak
# df'den birden fazla değişkeni ismiyle seçmek
col_names = ["age", "embarked", "alive"]
df.loc[0:3, col_names]


#######################
# Koşullu Seçim (Conditional Selection)
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df[df["age"] > 50].head()
df[df["age"] > 50]["age"].count()

df.loc[df["age"] > 50, ["age", "class"]].head()

df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

df["embark_town"].value_counts()

df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
       & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
       ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()

#############################################
# Toplulaştırma ve Gruplama (Aggregation & Grouping)
#############################################

# - count()
# - first()
# - last()
# - mean()
# - median()
# - min()
# - max()
# - std()
# - var()
# - sum()
# - pivot table

import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df["age"].mean()

df.groupby("sex")["age"].mean()

df.groupby("sex").agg({"age": "mean"})
df.groupby("sex").agg({"age": ["mean", "sum"]})

df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                       "survived": "mean"})

df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                       "survived": "mean"})


df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})


#######################
# Pivot table
#######################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", ["embarked", "class"])

df.head()

df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])

pd.set_option('display.width', 500)


#############################################
# Apply ve Lambda
#############################################
import pandas as pd
import seaborn as sns
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"]*2
df["age3"] = df["age"]*5

(df["age"]/10).head()
(df["age2"]/10).head()
(df["age3"]/10).head()

for col in df.columns:
    if "age" in col:
        print(col)

for col in df.columns:
    if "age" in col:
        print((df[col]/10).head())

for col in df.columns:
    if "age" in col:
        df[col] = df[col]/10

df.head()

df[["age", "age2", "age3"]].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: x/10).head()

df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()

def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()

df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

df.head()

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy_array as np
import pandas as pd
m = np.random.randint(1, 30, size=(5, 3))
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

pd.concat([df1, df2])

pd.concat([df1, df2], ignore_index=True)

#######################
# Merge ile Birleştirme İşlemleri
#######################

df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

pd.merge(df1, df2)
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)