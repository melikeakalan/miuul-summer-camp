# titanic: yolculuk esnasında meydana gelen kaza sonrasında
# yolcuların hayatta kalıp/kalmama durumlarını ifade eden veriseti
# survived: bağımlı değişken, hedef değişkendir. 1:yolcu hayatta kalmış, 0:yolcu hayatta kalamamış
# alive: hayatta kaldı mı, kalmadı mı? (yes/no)
# adult_male: yetişkin erkek mi? (true/false)
# alone: gemiye binen kişi yalnız mı? (true/false)
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

# cinsiyete göre yaş ortalaması
df.groupby("sex")["age"].mean()

# cinsiyete göre yaş ortalaması
# bu yöntem, yaş değişkenine birden fazla aggregate func. uygulamayı sağlar.
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

# console'da kod çıktısının bölünmemesi için
pd.set_option('display.width', 500)




