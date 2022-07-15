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
df.iloc[0:3]  # df'i 0. satırdan 3. satıra kadar getir
df.iloc[0, 0]  # df'nin 0. satır 0. sütundaki elemanını getir

# loc: label based selection, indexlerdeki label'lara göre seçim yapar
df.loc[0:3]  # df'yi 0. satırdan 3. satır dahil getirir

df.iloc[0:3, 0:3]  # df'yi 0. satırdan 3. satıra kadar, 0. sütundan 3. sütuna kadar getirir
df.loc[0:3, "age"]  # df'yi 0. satırdan 3. satır dahil, age sütunuyla getir

# loc'u fancy index ile kullanmak
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
# yaşı 50 den büyük olan kişi sayısı
df[df["age"] > 50]["age"].count()

# yaşı 50 den büyük olan kişileri sınıfıyla getir
df.loc[df["age"] > 50, ["age", "class"]].head()

# DIKKAT! Birden fazla koşul giriliyorsa bu durumda koşullar parantez içine alınmalıdır.
# yaşı 50 den büyük ve cinsiyeti erkek olan (df["age"] > 50) & (df["sex"] == "male")
df.loc[(df["age"] > 50) & (df["sex"] == "male"), ["age", "class"]].head()

# embark_town: gemiye binilen lokasyon
df["embark_town"].value_counts()

# df'yi üç farklı koşula göre ve koşul sütunlarıyla birlikte getir
df_new = df.loc[(df["age"] > 50) & (df["sex"] == "male")
                & ((df["embark_town"] == "Cherbourg") | (df["embark_town"] == "Southampton")),
                ["age", "class", "embark_town"]]

df_new["embark_town"].value_counts()