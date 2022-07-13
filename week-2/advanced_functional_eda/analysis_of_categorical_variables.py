#############################################
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
#############################################

# - kategorik değişken: category, bool ve  object tiplerinin hepsi
# - sinsirella değişken: tip bilgisi nümerik ama aslında kategorik olan
# - cardinality'si yüksek değişken: ölçülemeyecek kadar fazla sınıfı olan (ör. 50 sınıflı kategorik değişken)


import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
df = sns.load_dataset("titanic")
df.head()

df["sex"].dtypes
print(df["sex"].dtypes)
str(df["sex"].dtypes)

df["sex"].value_counts()  # değişkenin sınıfları ve sayıları
df["sex"].unique()        # değişkenin unique değerleri
df["sex"].nunique()       # değişkenin toplam unique sayısı

# bütün columnlarda gez, yakaladığın verilerin tip bilgisini kontrol et,
# eğer verilerin tipi "category", "object" veya "bool" barındırıyorsa bu verileri seç
cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]

# DIKKAT! survived değişkeninin tip bilgisi nümerik ama aslında kategorik
df["survived"].value_counts()
# 0    549
# 1    342
# Name: survived, dtype: int64


# tipi int ya da float olup eşsiz sınıf sayısı belirli bir değerden küçük olan değişkenleri yakala ve
# nümerik görünümlü ama kategorik değişkenine ata
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float"]]

# 2.yol int64, int32, float64, float32 tipinde olanların hepsini yakalamak için
num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and
               (str(df[col].dtypes).startswith(('int' or 'float')))]


# category görünümlü ama aslında cardinal olan değişkenlerin tespiti
cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]

# object, bool, category ve sinsirella değişkenlerin hepsi cat_cols'ta
cat_cols = cat_cols + num_but_cat

# cardinal değişkenler çıkarıldıktan sonra elde edilen esas cat_cols
cat_cols = [col for col in cat_cols if col not in cat_but_car]

# cat_cols'ta artık değişkenlerin tamamı kategoriktir.
df[cat_cols].nunique()

# cat_cols'ta olmayan yani nümerik değişkenler
[col for col in df.columns if col not in cat_cols]

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)


# kategorik değişkenin sınıflarını yüzdelik oranla veren function
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")

# veri setindeki bütün kategorik değişenler için sınıf oranlarını getir
for col in cat_cols:
    cat_summary(df, col)


def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


cat_summary(df, "sex", plot=True)

# veri setindeki bütün kategorik değişenler için sınıf oranlarını çizdir
# DIKKAT! countplot func. bool tipli verileri görselleştiremez.
for col in cat_cols:
    cat_summary(df, col, plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("sdfsdfsdfsdfsdfsd")
    else:
        cat_summary(df, col, plot=True)

# bool tipli değişken int'e çevrilir. (True --> 1, False --> 0)
# DIKKAT! int defaullta, int32 geliyor ama bizim verilerimiz int64 o yüzden 2. yolu kullanıyoruz.
# df["adult_male"].astype(int)     # 1. yol
df["adult_male"].astype('int64')   # 2. yol

# veri setindeki bütün kategorik değişenler için sınıf oranlarını çizdir
# DIKKAT! değişkeni özetleyen cat_summary func içine bu döngüyü yazmayız çünkü
# Her fonksiyonun tek bir görevi olmalıdır. Yani dataframdeki tüm değişkenleri özetlememeli.
for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype('int64')
        cat_summary(df, col, plot=True)

    else:
        cat_summary(df, col, plot=True)


# kategorik değişkenin sınıf oranlarını çizdiren, bool tipli olanları dönüştüren function
def cat_summary(dataframe, col_name, plot=False):
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype('int64')

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)
    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                            "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("##########################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


cat_summary(df, "adult_male", plot=True)


# old but gold :)
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")


cat_summary(df, "sex")
