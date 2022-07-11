#############################################
# NUMPY
#############################################

# Neden NumPy? (Why Numpy?)
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
# Yeniden Şekillendirme (Reshaping)
# Index Seçimi (Index Selection)
# Slicing
# Fancy Index
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
# Matematiksel İşlemler (Mathematical Operations)

#############################################
# Neden NumPy?
#############################################

# 1- Numpy, listelere göre daha hızlıdır çünkü sabit tipte veri tutar.
# 2- Yüksek seviyeden(vektörel) işlemler yapmayı sağlar. (a*b)

import numpy as np
a = [1, 2, 3, 4]
b = [2, 3, 4, 5]

ab = []

for i in range(0, len(a)):
    ab.append(a[i] * b[i])

a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 5])
a * b


#############################################
# NumPy Array'i Oluşturmak (Creating Numpy Arrays)
#############################################
import numpy as np

np.array([1, 2, 3, 4, 5])
type(np.array([1, 2, 3, 4, 5]))
np.zeros(10, dtype=int)            # array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
np.random.randint(0, 10, size=10)  # 0-10 arasında 10 elemanlı ndarray
np.random.normal(10, 4, (3, 4))    # ort. 10, std sapması 4, 3*4 lük normal dağılımlı ndarray


#############################################
# NumPy Array Özellikleri (Attibutes of Numpy Arrays)
#############################################
import numpy as np

# ndim: boyut sayısı
# shape: boyut bilgisi
# size: toplam eleman sayısı
# dtype: array veri tipi

a = np.random.randint(10, size=5)  # 0-10 arasında 5 elemanlı ndarray
a.ndim   # 1
a.shape  # (5,) tek boyutlu içerisinde 5 eleman var
a.size   # 5
a.dtype  # dtype('int32')

#############################################
# Yeniden Şekillendirme (Reshaping)
#############################################
import numpy as np

np.random.randint(1, 10, size=9)
# array([4, 5, 8, 6, 4, 4, 6, 2, 4])

# DIKKAT! size=10 olsaydı hata verirdi
np.random.randint(1, 10, size=9).reshape(3, 3)
# array([[7, 8, 1],
#        [3, 4, 9],
#        [1, 7, 2]])

ar = np.random.randint(1, 10, size=9)
# array([3, 7, 3, 1, 5, 9, 1, 6, 5])

ar.reshape(3, 3)
# array([[3, 7, 3],
#        [1, 5, 9],
#        [1, 6, 5]])


#############################################
# Index Seçimi (Index Selection)
#############################################
import numpy as np
a = np.random.randint(10, size=10)
# array([3, 5, 0, 5, 4, 4, 0, 5, 7, 8])

a[0]        # 3
a[0:5]      # array([3, 5, 0, 5, 4])  0. indexten 5. index'e kadar
a[0] = 999  # array([999, 5, 0, 5, 4, 4, 0, 5, 7, 8])

m = np.random.randint(10, size=(3, 5))
# array([[3, 7, 4, 4, 1],
#        [8, 4, 5, 4, 9],
#        [2, 4, 5, 1, 0]])

m[0, 0]  # 3  0. satırdaki 0. sütundaki eleman
m[1, 1]
m[2, 3]

m[2, 3] = 999
# array([[  3,   7,   4,   4,   1],
#        [  8,   4,   5,   4,   9],
#        [  2,   4,   5, 999,   0]])

# DIKKAT! numpy sabit tipte veri saklar, hem float hem int saklayamaz yani 2.9 değil 2'yi saklar.
m[2, 3] = 2.9
# array([[3, 7, 4, 4, 1],
#        [8, 4, 5, 4, 9],
#        [2, 4, 5, 2, 0]])

m[:, 0]      # array([3, 8, 2])  bütün satırları ve 0. sütunu seç
m[1, :]      # array([8, 4, 5, 4, 9])  1. satırı ve tüm sütunları seç

m[0:2, 0:3]  # 0'dan 2'ye kadar satırlarda, 0'dan 3'e kadar sütunlarda git
# array([[3, 7, 4],
#        [8, 4, 5]])

#############################################
# Fancy Index
#############################################

# Bir numpy array'ine bir liste girdiğimizde seçim yapmayı sağlar.( v[catch] )
# (liste, index numaralarını veya true/false ifadelerini tutabilir)

import numpy as np

v = np.arange(0, 30, 3)  # 0'dan 30'a kadar üçer üçer artacak şekilde array oluştur
# array([ 0,  3,  6,  9, 12, 15, 18, 21, 24, 27])

v[1]  # 3
v[4]

catch = [1, 2, 3]

v[catch]  # array([3, 6, 9])

#############################################
# Numpy'da Koşullu İşlemler (Conditions on Numpy)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

# Amaç: array içerisindeki 3'ten küçük olan değerlere erişmek

#######################
# Klasik döngü ile
#######################
ab = []
for i in v:
    if i < 3:
        ab.append(i)

ab  # [1, 2]

#######################
# Numpy ile
# Fancy index ile array'in içinden koşullu eleman seçmek
#######################
v < 3      # array([ True,  True, False, False, False])

v[v < 3]   # array([1, 2])
v[v > 3]
v[v != 3]
v[v == 3]  # array([3])
v[v >= 3]

#############################################
# Matematiksel İşlemler (Mathematical Operations)
#############################################
import numpy as np
v = np.array([1, 2, 3, 4, 5])

v / 5       # array([0.2, 0.4, 0.6, 0.8, 1. ])
v * 5 / 10  # array([0.5, 1. , 1.5, 2. , 2.5])
v ** 2      # array([ 1,  4,  9, 16, 25])
v - 1       # array([0, 1, 2, 3, 4])

np.subtract(v, 1)      # array([0, 1, 2, 3, 4])
np.add(v, 1)           # array([2, 3, 4, 5, 6])
np.mean(v)             # 3.0
np.sum(v)              # 15
np.min(v)              # 1
np.max(v)              # 5
np.var(v)              # 2.0  array'in varyansı
v = np.subtract(v, 1)  # permanent

#######################
# NumPy ile İki Bilinmeyenli Denklem Çözümü
#######################

# 5*x0 + x1 = 12
# x0 + 3*x1 = 10

a = np.array([[5, 1], [1, 3]])
b = np.array([12, 10])

np.linalg.solve(a, b)  # array([1.85714286, 2.71428571])