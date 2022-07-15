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

df.drop(0, axis=0).head()  # 0. satırı sil
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
df.age.head()  # variable selection

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

"age" in df  # değişken df'de var mı ?

df["age"].head()
df.age.head()

df["age"].head()
type(df["age"].head())  # pandas.core.series.Series

# DIKKAT! Tek bir değişken seçerken seçimin sonucunun df olarak kalması için [[]] kullanılmalı
df[["age"]].head()
type(df[["age"]].head())  # pandas.core.frame.DataFrame

# df'de birden çok değişken seçme
df[["age", "alive"]]

col_names = ["age", "adult_male", "alive"]
df[col_names]

# df'ye yeni bir değişken ekleme
df["age2"] = df["age"] ** 2
df["age3"] = df["age"] / df["age2"]

# df'den değişken silme
df.drop("age3", axis=1).head()

# df'de birden çok değişken silme
df.drop(col_names, axis=1).head()

# df'de belirli string ifadeyi barındıran değişkenleri silme
# bütün satırları seç, df'nin columnlarına string operation yapılacak ve contains method kullanılacak
# ~: column isimleri içerisinde "age"'i barındırmayan columnları getir.
df.loc[:, ~df.columns.str.contains("age")].head()
