#########################################
# Python Execises
#########################################

# GOREV -1: veri tiplerini sorgulayın, type() kullanın

x = 8
y = 3.2
z = 8J + 18
a = "HELLO WORLD"
b = True
c = 23 < 22
myList = [1, 2, 3, 4]
d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
t = ("Machine learning", "Data science")
s = {"Python", "Machine learning", "Data science"}

# ANSWER
print(type(x))  # int
print(type(y))  # float
print(type(z))  # complex
print(type(a))  # str
print(type(b))  # bool
print(type(c))  # bool
print(type(myList))  # list
print(type(d))  # dict
print(type(t))  # tuple
print(type(s))  # set

# GOREV -2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz.
#  Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.

text = "The goal is to turn data information, and information into insight."

# ANSWER
help(text.replace)
print(text.replace(",", " ").replace(".", " ").upper().split())
# ['THE', 'GOAL', 'IS', 'TO', 'TURN', 'DATA', 'INFORMATION', 'AND', 'INFORMATION', 'INTO', 'INSIGHT']


# GOREV -3: Verilen listeye aşağıdaki adımları uygulayınız.

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
"""
Adım1: Verilen listenin eleman sayısına bakınız.
Adım2: Sıfırıncı ve onuncu indeksteki elemanları çağırınız.
Adım3: Verilen liste üzerinden ["D", "A", "T", "A"] listesi oluşturunuz.
Adım4: Sekizinci indeksteki elemanı siliniz.
Adım5: Yeni bir eleman ekleyiniz.
Adım6: Sekizinci indekse"N" elemanını tekrar ekleyiniz. 
"""

# ANSWER
print(len(lst))  # 11
print(lst[0], lst[10])  # D E
new_list = lst[0:4]

print(lst[8])  # N
lst.pop(8)
print(lst)  # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'C', 'E']

lst.append("+")

lst.insert(8, "N")
print(lst)  # ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'C', 'E', '+']

# GOREV -4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.

dict = {'Christian': ["America", 18],
        'Daisy': ["England", 12],
        'Antonio': ["Spain", 22],
        'Dante': ["Italy", 25]}
"""
Adım1: Key değerlerine erişiniz.
Adım2: Value'lara erişiniz. 
Adım3: Daisy key'ine ait 12 değerini 13 olarak güncelleyiniz.
Adım4: Key değeri Ahmet value değeri [Turkey,24] olan yeni bir değer ekleyiniz.
Adım5: Antonio'yu dictionary'den siliniz.

"""

# ANSWER
dict.keys()  # dict_keys(['Christian', 'Daisy', 'Antonio', 'Dante'])
dict.values()  # dict_values([['America', 18], ['England', 12], ['Spain', 22], ['Italy', 25]])

dict.update({'Ahmet': ['Turkey', 24]})
print(dict)
# {'Christian': ['America', 18],
# 'Daisy': ['England', 12],
# 'Antonio': ['Spain', 22],
# 'Dante': ['Italy', 25],
# 'Ahmet': ['Turkey', 24]}

dict.pop('Antonio')  # del dict['Antonio]
print(dict)
# {'Christian': ['America', 18],
# 'Daisy': ['England', 12],
# 'Dante': ['Italy', 25],
# 'Ahmet': ['Turkey', 24]}


# GOREV -5: Argüman olarak birliste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atayan ve
#  bu listeleri return eden fonksiyon yazınız.

l = [2, 13, 18, 93, 22]


# ANSWER
def func(my_list):
    even_list = []
    odd_list = []

    for item in range(len(my_list)):
        if item % 2 == 0:
            even_list.append(item)
        else:
            odd_list.append(item)
    # [even_list.append(i) if i % 2 == 0 else odd_list.append(i) for i in my_list]

    return even_list, odd_list


even_list, odd_list = func([])  # even_list = [2, 4], odd_list = [1, 3]

# GOREV -6: List Comprehension yapısı kullanarak
#  car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
#  ipucu: Numeric olmayan değişkenlerin de isimleri büyümeli.Tek bir list comprehension yapısı kullanılmalı.


import seaborn as sns
df = sns.load_dataset("car_crashes")
df.columns
print(df)

# ANSWER
["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
# ['NUM_TOTAL',
#  'NUM_SPEEDING',
#  'NUM_ALCOHOL',
#  'NUM_NOT_DISTRACTED',
#  'NUM_NO_PREVIOUS',
#  'NUM_INS_PREMIUM',
#  'NUM_INS_LOSSES',
#  'ABBREV']


# GOREV -7: List Comprehension yapısı kullanarak
#  car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna"FLAG" yazınız.
#  ipucu: Tüm değişkenlerin isimleri büyük harf olmalı.Tek bir list comprehension yapısı ile yapılmalı.


# ANSWER
[col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
# ['TOTAL_FLAG',
#  'SPEEDING_FLAG',
#  'ALCOHOL_FLAG',
#  'NOT_DISTRACTED',
#  'NO_PREVIOUS',
#  'INS_PREMIUM_FLAG',
#  'INS_LOSSES_FLAG',
#  'ABBREV_FLAG']


# GOREV -8: List Comprehension yapısık ullanarak
#  aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir data frame oluşturunuz.
#  ipucu: Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
#  Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.

og_list = ["abbrev", "no_previous"]

# AMSWER
new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]
new_df.head()
#    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# 0   18.8     7.332    5.640          18.048       784.55      145.08
# 1   18.1     7.421    4.525          16.290      1053.48      133.93
# 2   18.6     6.510    5.208          15.624       899.47      110.35
# 3   22.4     4.032    5.824          21.056       827.34      142.39
# 4   12.0     4.200    3.360          10.920       878.41      165.63
