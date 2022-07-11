###############################################
# FONKSİYONLAR (FUNCTIONS)
###############################################

#######################
# Fonksiyon Okuryazarlığı
#######################

# python console'a ?print veya help(print) yazılarak, print'in dokümantasyonuna bakılır
# kullanacak olduğumuz bütün fonksiyonların bir dokümantasyonu vardır, bunlara docstring denir

print("a", "b")

print("a", "b", sep="__")


#######################
# Fonksiyon Tanımlama
#######################

def calculate(x):
    print(x * 2)


calculate(5)


# İki argümanlı/parametreli bir fonksiyon tanımlayalım.

def summer(arg1, arg2):
    print(arg1 - arg2)


summer(7, 8)  # -1

summer(8, 7)  # 1

summer(arg2=8, arg1=7)  # -1


#######################
# Docstring
#######################

def summer(arg1, arg2):
    print(arg1 + arg2)


# fonksiyona  """ docstring """ eklenir
def summer(arg1, arg2):
    """
    Sum of two numbers

    Args:
        arg1: int, float
        arg2: int, float

    Returns:
        int, float

    Examples:

    Notes:

    """

    print(arg1 + arg2)


summer(1, 3)


#######################
# Fonksiyonların Statement/Body Bölümü
#######################

# def function_name(parameters/arguments):
#     statements (function body)

def say_hi(integer):
    print("Merhaba")
    print("Hi")
    print("Hello")


say_hi(4)


def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")


say_hi("miuul")


def multiplication(a, b):
    c = a * b
    print(c)


multiplication(10, 9)

# girilen değerleri bir liste içinde saklayacak fonksiyon.

list_store = []


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 8)
add_element(18, 8)
add_element(180, 10)


#######################
# Ön Tanımlı Argümanlar/Parametreler (Default Parameters/Arguments)
#######################

def divide(a, b):
    print(a / b)


divide(1, 2)


def divide(a, b):
    print(a / b)


divide(10)  # b ön tanımlı olsaydı hata vermezdi


def say_hi(string="Merhaba"):
    print(string)
    print("Hi")
    print("Hello")


say_hi()
say_hi("mrb")

#######################
# Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?
#######################

# varm, moisture, charge

(56 + 15) / 80
(17 + 45) / 70
(52 + 45) / 80


# DRY

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


calculate(98, 12, 78)


#######################
# Return: Fonksiyon Çıktılarını Girdi Olarak Kullanmak
######################

def calculate(varm, moisture, charge):
    print((varm + moisture) / charge)


# calculate(98, 12, 78) * 10

def calculate(varm, moisture, charge):
    return (varm + moisture) / charge


calculate(98, 12, 78) * 10

a = calculate(98, 12, 78)


def calculate(varm, moisture, charge):
    varm = varm * 2
    moisture = moisture * 2
    charge = charge * 2
    output = (varm + moisture) / charge
    return varm, moisture, charge, output


type(calculate(98, 12, 78))

varma, moisturea, chargea, outputa = calculate(98, 12, 78)


#######################
# Fonksiyon İçerisinden Fonksiyon Çağırmak
######################

def calculate(varm, moisture, charge):
    return int((varm + moisture) / charge)


calculate(90, 12, 12) * 10


def standardization(a, p):
    return a * 10 / 100 * p * p


standardization(45, 1)


# DİKKAT!

# Eğer tanımlanacak ana fonk. içerisinde başka fonksiyonlar(calculate, standardization)  çağrılacaksa,
# çağıralacak fonksiyonların argümanları da tanımlanan ana fonksiyon içerisinde biçimlendirilecekse,
# ana fonksiyonu tanımlarken çağrılacak fonksiyonların argümanları da girilmelidir.(varm, moisture, charge, p)

def all_calculation(varm, moisture, charge, p):
    a = calculate(varm, moisture, charge)
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 12)


def all_calculation(varm, moisture, charge, a, p):
    print(calculate(varm, moisture, charge))
    b = standardization(a, p)
    print(b * 10)


all_calculation(1, 3, 5, 19, 12)

#######################
# Lokal & Global Değişkenler (Local & Global Variables)
#######################

list_store = [1, 2]


def add_element(a, b):
    c = a * b
    list_store.append(c)
    print(list_store)


add_element(1, 9)