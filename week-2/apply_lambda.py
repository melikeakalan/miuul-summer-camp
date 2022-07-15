#############################################
# Apply ve Lambda
#############################################
# Apply: döngü yazmadan elimizdeki belirli bir fonksiyonu satırlara ya da sütunlara uygulamayı sağlar.
# Lambda: func. tanımlama şeklidir. def'ten farkı kullan-at fonksiyondur.

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["age2"] = df["age"] * 2
df["age3"] = df["age"] * 5

(df["age"] / 10).head()
(df["age2"] / 10).head()
(df["age3"] / 10).head()

# df'nin sütun isimlerinde "age" varsa bu sütunları yaz
for col in df.columns:
    if "age" in col:
        print(col)

# df'nin sütun isimlerinde "age" varsa bu sütun değerlerini 10'a böl
for col in df.columns:
    if "age" in col:
        print((df[col] / 10).head())

# df'nin sütun isimlerinde "age" varsa bu sütun değerlerini 10'a böl ve df'ye kaydet
for col in df.columns:
    if "age" in col:
        df[col] = df[col] / 10

df.head()

# değişkenleri seç ve bunlara kendisine girilen ifadenin 10'a bölümünü uygula
df[["age", "age2", "age3"]].apply(lambda x: x / 10).head()

# tüm satırları seç, sütunlardan "age'i" barındıranları seç ve yine aynı func. uygula
df.loc[:, df.columns.str.contains("age")].apply(lambda x: x / 10).head()

# func. uygulandığı df'deki değerleri standart hale getirsin (normalleştirsin)
df.loc[:, df.columns.str.contains("age")].apply(lambda x: (x - x.mean()) / x.std()).head()


def standart_scaler(col_name):
    return (col_name - col_name.mean()) / col_name.std()


# önceden tanımlanmış fonksiyonu da apply ile kullanabiliriz
df.loc[:, df.columns.str.contains("age")].apply(standart_scaler).head()

# df.loc[:, ["age","age2","age3"]] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)

# df'ye yaptığımız değişiklikleri yine df'ye kaydettik
df.loc[:, df.columns.str.contains("age")] = df.loc[:, df.columns.str.contains("age")].apply(standart_scaler)


df.head()