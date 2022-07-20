###############################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
# #############################################

"""
İş Problemi:
Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
seviye tabanlı (level based) yeni müşteri tanımları (persona)
oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
istemektedir.

Örneğin:
Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
isteniyor.

Veri Seti Hikayesi:
Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
kullanıcı birden fazla alışveriş yapmış olabilir.

Değişkenler:
PRICE   – Müşterinin harcama tutarı
SOURCE  – Müşterinin bağlandığı cihaz türü
SEX     – Müşterinin cinsiyeti
COUNTRY – Müşterinin ülkesi
AGE     – Müşterinin yaşı
"""

#############################################
# Proje Görevleri
#############################################

#############################################
# Görev 1: Aşağıdaki Soruları Yanıtlayınız
#############################################

# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
import pandas as pd

df = pd.read_csv("week-2/project/persona.csv")
df.head()
df.info()
df.isnull().values.any()

#  Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Soru 3: Kaç unique PRICE vardır
df["PRICE"].nunique()

# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df["PRICE"].value_counts()

# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df["COUNTRY"].value_counts()


# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

# 1. yol pivot table
df.pivot_table(values="PRICE", index="COUNTRY", aggfunc="sum")

# 2. yol group by
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Soru 7: SOURCE türlerine göre satış sayıları nedir?
df["SOURCE"].value_counts()
df.pivot_table("PRICE", "SOURCE", aggfunc="count")
df.groupby("SOURCE")["PRICE"].count()

# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.pivot_table("PRICE", "COUNTRY")
df.groupby(by=['COUNTRY']).agg({"PRICE": "mean"})

# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.pivot_table("PRICE", "SOURCE")
df.groupby(by=['SOURCE']).agg({"PRICE": "mean"})

# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.pivot_table("PRICE", ["COUNTRY", "SOURCE"])
df.groupby(by=["COUNTRY", 'SOURCE']).agg({"PRICE": "mean"})


#############################################
# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
#############################################
df.pivot_table("PRICE", ["COUNTRY", "SOURCE", "SEX", "AGE"])
df.groupby(["COUNTRY", 'SOURCE', "SEX", "AGE"]).agg({"PRICE": "mean"})
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean()


#############################################
# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
#############################################

# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz.

# 1. yol pivot table
agg_df = df.pivot_table("PRICE", ["COUNTRY", "SOURCE", "SEX", "AGE"]).sort_values("PRICE", ascending=False)

# 2. yol group by
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)
# Not: df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"])["PRICE"].mean() olarak kurgularsanız,
# çıktınız pandas.core.series.Series tipinde olacağından "sort_values" yapamazsınız.


#############################################
# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
#############################################

# Görev 3'ün çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir.
# Bu isimleri değişken isimlerine çeviriniz.

agg_df = agg_df.reset_index()


#############################################
# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
#############################################

# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'

agg_df["AGE"].max()

# AGE değişkeninin nerelerden bölüneceğini belirtelim:
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]

# Bölünen noktalara karşılık isimlendirmelerin ne olacağını ifade edelim:
mylabels = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df["AGE"].max())]

# age'i bölelim:
agg_df["age_cat"] = pd.cut(agg_df["AGE"], bins, labels=mylabels)
agg_df.head()


#############################################
# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
#############################################

# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturun.
# Dikkat!
# Listcomprehensionile customers_level_based değerleri oluşturulduktan sonra bu değerlerin
# tekilleştirilmesi gerekmektedir. Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18.
# Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.

# değişken isimleri:
agg_df.columns

# gözlem değerleri:
agg_df.values

agg_df["customers_level_based"] = [country.upper() + "_" + source.upper() + "_" +
        sex.upper() + "_" + age_cat.upper() for country, source, sex, age_cat
        in zip(agg_df["COUNTRY"], agg_df["SOURCE"], agg_df["SEX"], agg_df["age_cat"])]

agg_df["customers_level_based"].nunique()  # 109
agg_df["customers_level_based"].count()    # 348

agg_df = agg_df.groupby(["customers_level_based"]).agg({"PRICE": "mean"})
agg_df = agg_df.reset_index()


#############################################
# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
#############################################

# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

# qcut: price değerlerini küçükten büyüğe sıralayıp quantile lara göre parçalar.
# A segmentindeki müşteriler, en çok alış-veriş yapanlar
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], q=4, labels=["D", "C", "B", "A"])


def analysis_segments(df):
    segment_list = list(df["SEGMENT"].unique())
    for segment in segment_list:
        print("Segment: ", segment,
              "\n", df[df["SEGMENT"] == segment].agg({"PRICE": ["mean", "max", "sum"]}), end="\n\n")


analysis_segments(agg_df)


#############################################
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini  tahmin ediniz.
#############################################


def guess_income(user_segment): return list(agg_df[agg_df["customers_level_based"] == user_segment]["SEGMENT"]),\
                                       float(agg_df[agg_df["customers_level_based"] == user_segment]["PRICE"])


# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

# 1. yol
user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == user]

# 2. yol
user_1 = "TUR_ANDROID_FEMALE_31_40"
guess_income(user_1)


# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == user]


