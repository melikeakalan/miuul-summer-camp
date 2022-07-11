#######################
# Uygulama - Mülakat Sorusu-1
#######################

# Amaç: Aşağıdaki şekilde string değiştiren fonksiyon yazmak istiyoruz.
# before: "hi my name is john and i am learning python"
# after: "Hi mY NaMe iS JoHn aNd i aM LeArNiNg pYtHoN"

def alternating(string):
    new_string = ""
    # girilen string'in index'lerinde gez.
    for string_index in range(len(string)):
        # index çift ise büyük harfe çevir.
        if string_index % 2 == 0:
            new_string += string[string_index].upper()
        # index tek ise küçük harfe çevir.
        else:
            new_string += string[string_index].lower()
    print(new_string)


alternating("melike")

#######################
# Uygulama - Mülakat Sorusu-2
#######################

# divide_students fonksiyonu yazınız.
# Çift indexte yer alan öğrencileri bir listeye alınız.
# Tek indexte yer alan öğrencileri başka bir listeye alınız.
# Fakat bu iki liste tek bir liste olarak return olsun.

students = ["John", "Mark", "Venessa", "Mariam"]


def divide_students(students):
    groups = [[], []]
    for index, student in enumerate(students):
        if index % 2 == 0:
            groups[0].append(student)
        else:
            groups[1].append(student)
    print(groups)
    return groups


st = divide_students(students)
st[0]
st[1]


#######################
# alternating fonksiyonunun enumerate ile yazılması
#######################

def alternating_with_enumerate(string):
    new_string = ""
    for i, letter in enumerate(string):
        if i % 2 == 0:
            new_string += letter.upper()
        else:
            new_string += letter.lower()
    print(new_string)


alternating_with_enumerate("i love python -_-")

#######################
# Uygulama - Mülakat Sorusu-3
#######################

# Amaç: çift sayıların karesi alınarak bir sözlüğe eklenmek istemektedir.
# Key'ler orjinal değerler value'lar ise değiştirilmiş değerler olacak.

numbers = range(10)

# 1. yol
new_dict = {}
for n in numbers:
    if n % 2 == 0:
        new_dict[n] = n ** 2

# 2. yol: dictionary comprehension
{n: n ** 2 for n in numbers if n % 2 == 0}
