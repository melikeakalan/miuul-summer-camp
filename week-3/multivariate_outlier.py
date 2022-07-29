#############################################
# Çok Değişkenli Aykırı Değer Analizi: Local Outlier Factor
#############################################

# Tek başına aykırı olamayacak değerler, birlikte ele alındığında aykırılık yaratıyor olabilir.
# ör. yaş değişkeni ve evlenme değişkenleri olsun. 18 yaşında olup 3 defa evlenmiş olmak anormaldir.

# LOF Yöntemi,
# gözlemleri bulundukları konumda yoğunluk tabanlı skorlayarak aykırı değerleri bu skora göre bulur.
# A noktası, aykırı değerdir(outlier).
# İki boyutlu gösterimde, her bir nokta(gözlem) için bir skor değeri verilir.
# İlgili gözlemin skoru 1'den uzaklaştıkça outlier olma ihtimali artar.
# Threshold değerini belirleyip yine kendimiz de aykırı değerleri belirleyebiliriz.

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.neighbors import LocalOutlierFactor

from outliers import outlier_thresholds, check_outlier

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)
pd.set_option('display.width', 500)


# diamonds veri setinin sayısal değişkenlerini, eksik değerlerini drop ederek getir
df = sns.load_dataset('diamonds')
df = df.select_dtypes(include=['float64', 'int64'])
df = df.dropna()
df.head()
df.shape

for col in df.columns:
    print(col, check_outlier(df, col))

low, up = outlier_thresholds(df, "carat")
# carat değişkeninde 1889 tane aykırı değer var
df[((df["carat"] < low) | (df["carat"] > up))].shape

low, up = outlier_thresholds(df, "depth")
# depth değişkeninde 2545 tane aykırı değer var
df[((df["depth"] < low) | (df["depth"] > up))].shape


"""
# Dikkat! outlier threshold literatürde 25'e 75'likti fakat biz 5'e 95 kullanacağız. Çünkü çok fazla aykırı değer varsa
# bunları silersek veri kaybı çok olur, baskılama yaparsak da çok fazla gürültü eklenmiş olur. 
# Ağaç yöntemleriyle çalışıyorsak bu outlier gözlemlere hiç dokunmamalıyız.
# Ya da 99'a 1'lik veya 95'e 5'lik gibi iqr hesaplanır, bu hesaplama üzerinden aykırı gözlemler veri setinden çıkarılır"""

clf = LocalOutlierFactor(n_neighbors=20)
clf.fit_predict(df)

df_scores = clf.negative_outlier_factor_
df_scores[0:5]


"""
# score'ları pozitif de yapabiliriz fakat bunu yapmayacağız.
# Çünkü eşik değere karar vermek için elbow method kullanıldığında grafiğin daha rahat okunmasını istiyoruz.
# Dikkat!
# Score'lar negatif olduğundan -1'den uzaklaştıkça(-10'a doğru) outlier olma ihtimali artar. """

# df_scores = -df_scores
np.sort(df_scores)[0:5]


"""
LOF yönteminde outliers belirlemek için kullanacağımız threshold'u elbow methodu ile belirliyouz.
threshold'u -4.98'ten küçük olanlar aykırı değer kabul edilecek.
"""
scores = pd.DataFrame(np.sort(df_scores))
scores.plot(stacked=True, xlim=[0, 50], style='.-')
plt.show()

th = np.sort(df_scores)[3]

df[df_scores < th]


"""
dataframe'in aykrı değerleri ve bu aykırlıkların birbiriyle ilişkisi
ör. İkinci satırdaki aykırı değerde z değeri max değerini almış. Aykırılık durumu z'den kaynaklanıyor olabilir.
Yani z özelliği max iken diğer bazı özelliklerin böyle olamayacağını söyler.
Aykırı değerleri daha sonra drop ile sildik, inplace kullanmadığımız için kalıcı olarak silmedik."""
df[df_scores < th].shape
df.describe([0.01, 0.05, 0.75, 0.90, 0.99]).T

df[df_scores < th].index

df[df_scores < th].drop(axis=0, labels=df[df_scores < th].index)
