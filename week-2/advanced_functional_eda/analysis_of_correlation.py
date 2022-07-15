#############################################
# 5. Korelasyon Analizi (Analysis of Correlation)
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib

matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = pd.read_csv("week-2/datasets/breast_cancer.csv")

# id, unnamed değişkenlerini df'den çıkart
df = df.iloc[:, 1:-1]
df.head()
df.info()

df2 = sns.load_dataset("titanic")
df2.info()

num_cols_2 = [col for col in df2.columns if df2[col].dtypes in ['int64', 'float32']]
type(num_cols_2)

num_cols = [col for col in df.columns if df[col].dtype in [int, float]]
type(num_cols)

# bütün değişkenlerin birbiriyle korelasyonunu hesapla
corr = df[num_cols].corr()

# koyu mavi: pozitif korelasyon, koyu kırmızı: negatif korelasyon
# veri setindeki değişkenlerin korelasyonunu gösteren ısı haritası
sns.set(rc={'figure.figsize': (12, 12)})
sns.heatmap(corr, cmap="RdBu")
plt.show()

#######################
# Yüksek Korelasyonlu Değişkenlerin Silinmesi
#######################
# Her veri setinde bu işlem yapılmaz
# fakat büyük veri setlerinde birbirine benzer birçok değişken olabilir bu durumda kullanabiliriz.

# korelasyonların hepsi pozitif hale getirilir
cor_matrix = df.corr().abs()

# dört değişkenli bir veri setinin korelasyon çıktısı
# DIKKAT! matrise gereksiz elemanlar var, iki kez aynı değişkenlerin birbiriyle olan korelasyonu verilmiş
#           0         1         2         3
# 0  1.000000  0.117570  0.871754  0.817941
# 1  0.117570  1.000000  0.428440  0.366126
# 2  0.871754  0.428440  1.000000  0.962865
# 3  0.817941  0.366126  0.962865  1.000000

# Köşegen elamanlar, ve altındakiler aynı değişken korelasyonlarına karşılık geldiği için silinir
#     0        1         2         3
# 0 NaN  0.11757  0.871754  0.817941
# 1 NaN      NaN  0.428440  0.366126
# 2 NaN      NaN       NaN  0.962865
# 3 NaN      NaN       NaN       NaN

# NOTE
k = np.array([0, 1, 2, 3, 0.3, 0.9]).astype(bool)
# array([False,  True,  True,  True,  True,  True])

# 1'lerden oluşan, oluşturduğumuz matrisin boyutunda ndarray oluştur,
# bu ndarray'ini bool'a çevir, np.triu ile yukarıdaki gibi üst üçgen matris elde et
# üçgen matrisin üstündeki değerler True olacağından dolayı bunları where ile cor_matrix'e gönder
upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))
drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > 0.90)]
cor_matrix[drop_list]
df.drop(drop_list, axis=1)


def high_correlated_cols(dataframe, plot=False, corr_th=0.90):
    corr = dataframe.corr()
    cor_matrix = corr.abs()
    upper_triangle_matrix = cor_matrix.where(np.triu(np.ones(cor_matrix.shape), k=1).astype(bool))

    # columnlardan herhangi birisi, verilen threshold'dan büyükse sil
    drop_list = [col for col in upper_triangle_matrix.columns if any(upper_triangle_matrix[col] > corr_th)]
    if plot:
        import seaborn as sns
        import matplotlib.pyplot as plt
        sns.set(rc={'figure.figsize': (15, 15)})
        sns.heatmap(corr, cmap="RdBu")
        plt.show()
    return drop_list


high_correlated_cols(df)
drop_list = high_correlated_cols(df, plot=True)

# Yüksek Korelasyonlu Değişkenler Silindikten sonraki hali
df.drop(drop_list, axis=1)
high_correlated_cols(df.drop(drop_list, axis=1), plot=True)


# Yaklaşık 600 mb'lık 300'den fazla değişkenin olduğu bir veri setinde deneyelim.
# https://www.kaggle.com/c/ieee-fraud-detection/data?select=train_transaction.csv

df = pd.read_csv("../../fraud_train_transaction.csv")
len(df.columns)
df.head()

drop_list = high_correlated_cols(df, plot=True)

len(df.drop(drop_list, axis=1).columns)

# type(adsa)

a=np.random.randint(10, size=4)
a.no