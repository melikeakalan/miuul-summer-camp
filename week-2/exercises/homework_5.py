##################################################
# Pandas Exercises
##################################################

# Note: fanc-index her zaman loc, group by, pivot table yöntemlerinden daha hızlı çalışır.

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.info()


#########################################
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################
df['sex'].value_counts()

# yolcu sayılarını yüzdelik oranla görmek için
df['sex'].value_counts(normalize=True)


#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################
df.nunique()


#########################################
# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
#########################################
df["pclass"].nunique()


#########################################
# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################
df[["pclass", "parch"]].nunique()


#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
#########################################
df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype


#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################
df[df["embarked"] == 'C']


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz
#########################################
df[df["embarked"] != 'S']
df[~(df["embarked"] == "S")]  # 2. yol


#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################
# DIKKAT! fancy-index her zaman daha hızlı çalışır. Soruyu önce fancy-index ile çözmeyi dene.

# 1. yol fancy index
df[(df["age"] < 30) & (df["sex"] == "female")]

# 2. yol loc
new_df = df.loc[(df["age"] < 30) & (df["sex"] == "female")]

# 3. yol query
print(df.query('(age < 30) & (sex == "female")'))


#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70’den büyük yolcuların bilgilerini gösteriniz.
#########################################

# 1. yol fancy index
df[(df["fare"] > 500) | (df["age"] > 70)].head()

# 2. yol loc
df.loc[(df["fare"] > 500) | (df["age"] > 70)]


#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################
df.isnull().sum()


#########################################
# Görev 12: who değişkenini dataframe’den çıkarınız.
#########################################

# 1. yol drop method
df.drop("who", axis=1, inplace=True)

# 2. yol list comprehension
new_cols = [col for col in df.columns if col not in df[["who"]]]
df[new_cols].head()


#########################################
# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()


#########################################
# Görev 14: age değişkenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
#########################################
df["age"].fillna(df["age"].median(), inplace=True)


#########################################
# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################
df.pivot_table("survived", "pclass", "sex", aggfunc=(["sum", "count", "mean"]))
df.groupby(["sex", "pclass"]).agg({"survived": ["sum", "count", "mean"]})  # 2. yol


#########################################
# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 verecek bir fonksiyon yazın.
#########################################

# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz.
# (apply ve lambda yapılarını kullanınız)


# 1. yol
def age_30(age):
    if age < 30:
        return 1
    else:
        return 0


df["age_flag"] = df["age"].apply(lambda x: age_30(x))

# 2. yol
age_flag = df["age"].apply(lambda x: 1 if x < 30 else 0)
df["age_flag"] = age_flag
df.head()


#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################
df_tips = sns.load_dataset("tips")
df_tips.info()


#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerinin
# sum, min, max ve mean değerlerini bulunuz
#########################################
df_tips.pivot_table("total_bill", "time", aggfunc=("sum", "min", "max", "mean"))
df_tips.groupby("time").agg({"total_bill": ["sum", "min", "max", "mean"]})  # 2. yol


#########################################
# Görev 19: Day ve time’a göre total_bill değerlerinin sum, min, max ve mean değerlerini bulunuz.
#########################################
df_tips.pivot_table("total_bill", "day", "time", aggfunc=("sum", "min", "max", "mean"))
df_tips.groupby(["day", "time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})  # 2. yol


#########################################
# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre
# sum, min, max ve mean değerlerini bulunuz.
#########################################

# DIKKAT! Önce şartı sağlayan verileri seç sonra grupla

# 1. yol fancy index
df[(df["time"] == "lunch") & (df["sex"] == "Female")]. \
    groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})

# 2. yol pivot table
df_tips.loc[(df_tips["time"] == "Lunch") & (df_tips["sex"] == "Female")]. \
    pivot_table(["total_bill", "tip"], "day", aggfunc=("sum", "min", "max", "mean"))

# 3. yol group by
df_tips.loc[(df_tips["time"] == "Lunch") & (df_tips["sex"] == "Female")]. \
    groupby("day").agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})


#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
#########################################

# 1. yol fancy index
df_tips[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10)]["total_bill"].mean()

# 2. yol loc
df_tips.loc[(df_tips["size"] < 3) & (df_tips["total_bill"] > 10), "total_bill"].mean()


#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz.
# Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################
df_tips["total_bill_tip_sum"] = df_tips["total_bill"] + df_tips["tip"]


#########################################
# Görev 23: Total_bill değişkeninin kadın ve erkek için ayrı ayrı ortalamasını bulunuz.
#########################################

# Bulduğunuz ortalamaların altında olanlara 0, üstünde ve eşit olanlara 1 verildiği yeni bir total_bill_flag değişkeni
# oluşturunuz.Kadınlar için Female olanlarının ortalamaları, erkekler için ise Male olanların ortalamaları dikkate
# alınacaktır.Parametre olarak cinsiyet ve total_bill alan bir fonksiyon yazarak başlayınız.(If-else koşulları içerecek)

# 1. yol fancy index
f_avg = df_tips[df_tips["sex"] == "Female"]["total_bill"].mean()
m_avg = df_tips[df_tips["sex"] == "Female"]["total_bill"].mean()

# 2. yol loc
f_avg = df_tips["total_bill"].loc[df_tips["sex"] == "Female"].mean()
m_avg = df_tips["total_bill"].loc[df_tips["sex"] == "Male"].mean()

# 3. yol group by
f_avg = df_tips.groupby("sex").agg({"total_bill": "mean"})[0]
m_avg = df_tips.groupby("sex").agg({"total_bill": "mean"})[1]

df_tips["sex"].isnull().sum()


def flag_func(sex, total_bill):
    if sex == "Female":
        if total_bill < f_avg:
            return 0
        else:
            return 1
    else:
        if total_bill < m_avg:
            return 0
        else:
            return 1


df_tips["total_bill_flag"] = df_tips.apply(lambda x: flag_func(x.sex, x.total_bill), axis=1)


#########################################
# Görev 24: total_bill_flag değişkenini kullanarak cinsiyetlere göre
# ortalamanın altında ve üstünde olanların sayısını gözlemleyiniz.
#########################################

# 1. yol
df_tips.loc[df_tips["total_bill_flag"] == 1].value_counts()
df_tips.loc[df_tips["total_bill_flag"] == 0].value_counts()

# 2. yol
df_tips.groupby("sex")["total_bill_flag"].value_counts()

# 3. yol
df_tips.groupby(["sex", "total_bill_flag"]).total_bill_flag.count()

# 4. yol
df_tips.groupby(["sex", "total_bill_flag"]).agg({"total_bill_flag": "count"})


#########################################
# Görev 25: Veriyi total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve
# ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################
new_df_tips = df_tips.sort_values("total_bill_tip_sum", ascending=False).head(30)
new_df_tips
