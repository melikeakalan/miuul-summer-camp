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
# ignore_index: indexleri sıfırlar, yeniden oluşturur.
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