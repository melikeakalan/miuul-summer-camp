# titanic: yolculuk esnasında meydana gelen kaza sonrasında
# yolcuların hayatta kalıp/kalmama durumlarını ifade eden veriseti
# survived: bağımlı değişken, hedef değişkendir. 1:yolcu hayatta kalmış, 0:yolcu hayatta kalamamış
# alive: hayatta kaldı mı, kalmadı mı ? (yes/no)
# alone: gemiye binen kişi yalnız mı, değil mi ? (true/false)
# embark_town: gemiye binilen şehir
# embarked: gemiye binilen liman(C, Q, S)

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

# veri setinin yaş ortalaması
df["age"].mean()

# cisiyete göre yaş ortalaması
df.groupby("sex")["age"].mean()

# cinsiyete göre yaş ortalaması
# bu yöntem, yaş değişkenine birden fazla aggregate func. uygulayamayı sağlar.
df.groupby("sex").agg({"age": "mean"})

# cinsiyete göre yaş ortalaması ve toplamı
df.groupby("sex").agg({"age": ["mean", "sum"]})

# gemiye binen kadınların ve erkeklerin yüzde kaçı hayatta kalmış ?
df.groupby("sex").agg({"age": ["mean", "sum"],
                       "survived": "mean"})
#               age            survived
#              mean       sum      mean
# sex
# female  27.915709   7286.00  0.742038
# male    30.726645  13919.17  0.188908


df.groupby(["sex", "embark_town"]).agg({"age": ["mean"],
                                        "survived": "mean"})

# veri setini üç farklı değişkene göre ayırma ve birden çok aggregare func. göre gruplama
df.groupby(["sex", "embark_town", "class"]).agg({"age": ["mean"],
                                                 "survived": "mean"})

# DIKKAT! Yukarıdaki örneğe frekans bilgisi eklersek,
# kaç kişide yüzde kaçının hayatta kaldığına bu şekilde erişebiliriz
# ör. kadın yolcu olup, Cherbourg'dan gemiye binen ve  first class olan 43 yolcudan %97'si hayatta kalmış.
df.groupby(["sex", "embark_town", "class"]).agg({
    "age": ["mean"],
    "survived": "mean",
    "sex": "count"})

#######################
# Pivot table
#######################
# group by işlemlerine benzer şekilde veri setini kırılımlar açısından değerlendirmek ve
# ilgilendiğimiz özet istatistiği bu kırılımlar açısından görmeyi sağlar.

import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
df = sns.load_dataset("titanic")
df.head()

# 1. argüman: values, kesisişimde gösterilecek değişken
# 2. argüman: indexte(satırda) gösterilecek değişken
# 3. argüman: sütunda gösterilecek değişken
# pivot table'ın aggfunc. default değeri mean'dir. Kesişimlerinde survived değişkenin ortalaması olur.
df.pivot_table("survived", "sex", "embarked")

df.pivot_table("survived", "sex", "embarked", aggfunc="std")

# pivot table sütunlarında birden fazla değişken gösterme ("embarked", "class")
df.pivot_table("survived", "sex", ["embarked", "class"])

# pivot table sütunlarında ve satırlarında birden fazla değişken gösterme
df.pivot_table("survived", ["sex", "who"], ["embarked", "class"])

df.head()

# DIKKAT! cut ve qcut func. sayısal değişkenleri, kategorik değişkene çevirir
# cut:  sayısal değişkenin bölüneceği kategoriler belirtilecekse kullanılır
# qcut: otomatik olarak değerleri küçükten büyüğe sıralar ve yüzdelik çeyrek değerlerine göre kategorilere böler.
# bins: 25 < category_1  <= 40,   40 < cateogroy_2 <= 90
df["new_age"] = pd.cut(df["age"], [25, 40, 90])

df.pivot_table("survived", "sex", "new_age")
# new_age  (25, 40]  (40, 90]
# sex
# female   0.802198  0.770833
# male     0.220930  0.176471


df["new_age"] = pd.cut(df["age"], [0, 10, 18, 25, 40, 90])

df.pivot_table("survived", "sex", ["new_age", "class"])

# console'da kodun çıktısının bölünmemesi için
pd.set_option('display.width', 500)

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

#############################################
# Birleştirme (Join) İşlemleri
#############################################
import numpy as np
import pandas as pd

m = np.random.randint(1, 30, size=(5, 3))

# 1. argüman: dataframe'e çevrilecek veri yapısı  2. argüman: oluşacak dataframe'in değişken isimleri
df1 = pd.DataFrame(m, columns=["var1", "var2", "var3"])
df2 = df1 + 99

# DIKKAT! concat, defaultta axis=0 dır yani df'leri alt alta birleştirir
# Eğer birleştime işlemi yan yana yapılacaksa axis=1 yapılır
pd.concat([df1, df2])

# DIKKAT! yukarıdaki gibi iki df'yi birleştirdiğimizde ikişer kez aynı indexleri görürüz
# ignore_index: indexlerin sıfırlar, yeniden oluşturur.
pd.concat([df1, df2], ignore_index=True)

#######################
# Merge ile Birleştirme İşlemleri
#######################

# df1: çalışanlar ve çalışanların bağlı olduğu depertmanlar
df1 = pd.DataFrame({'employees': ['john', 'dennis', 'mark', 'maria'],
                    'group': ['accounting', 'engineering', 'engineering', 'hr']})

# df2: çalışanlar ve çalışanların işe başlangıç tarihleri
df2 = pd.DataFrame({'employees': ['mark', 'john', 'dennis', 'maria'],
                    'start_date': [2010, 2009, 2014, 2019]})

# her çalışanı işe başlangıç tarihiyle getir
pd.merge(df1, df2)

# birleştirme işlemi, employees değişkenine göre yapılsın
pd.merge(df1, df2, on="employees")

# Amaç: Her çalışanın müdürünün bilgisine erişmek istiyoruz.
df3 = pd.merge(df1, df2)

df4 = pd.DataFrame({'group': ['accounting', 'engineering', 'hr'],
                    'manager': ['Caner', 'Mustafa', 'Berkcan']})

pd.merge(df3, df4)
